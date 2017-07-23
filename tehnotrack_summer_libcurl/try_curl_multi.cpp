#include <iostream>
#include <iomanip>
#include <curl/curl.h>

// for usleep
#include <unistd.h>

size_t write_data(void *buffer, size_t size, size_t nmemb, void *userp)
{
   return size * nmemb;
}

int main(int argc, char* argv[])
{
    if (argc < 2) {
        std::cout << "Usage my_curl <urls...>" << std::endl;
        return 0;
    }
    //CURL *handle = curl_easy_init();
    CURLM *multi_handle = curl_multi_init();

    const int files_count = argc - 1;
    CURL **handles = new CURL* [files_count];
    for(int i = 0; i < files_count; i++) {
        handles[i] = curl_easy_init();
        curl_easy_setopt(handles[i], CURLOPT_URL, argv[i+1]);
        curl_easy_setopt(handles[i], CURLOPT_WRITEFUNCTION, write_data);
        curl_multi_add_handle(multi_handle, handles[i]);
    }

    int running_handles;
    curl_multi_perform(multi_handle, &running_handles);
    while(running_handles > 0) {
        curl_multi_perform(multi_handle, &running_handles);
        for(int i = 0; i < files_count; i++) {
            std::cout << "file " << i << ": ";
            double size_downloaded;
            double content_length;
            curl_easy_getinfo(handles[i], CURLINFO_CONTENT_LENGTH_DOWNLOAD, &content_length);
            curl_easy_getinfo(handles[i], CURLINFO_SIZE_DOWNLOAD, &size_downloaded);
            if (size_downloaded > 0) {
                std::cout << "Downloading... "
                          << std::setprecision(3) << size_downloaded / content_length * 100 << "%... "
                          << std::setprecision(10) << size_downloaded
                          << " bytes of " << content_length << std::endl;
            } else {
                std::cout << "Connecting..." << std::endl;
            }
        }
        std::cout << "\t----****----" << std::endl;
        usleep(1000000);
    }

    for (int i = 0; i < files_count; i++) {
        std::cout << "file " << i << ": ";
        double size_downloaded;
        double speed;
        curl_easy_getinfo(handles[i], CURLINFO_SIZE_DOWNLOAD, &size_downloaded);
        curl_easy_getinfo(handles[i], CURLINFO_SPEED_DOWNLOAD, &speed);
        std::cout << "Downloaded " << size_downloaded << " bytes at speed " << speed << " bytes/sec." << std::endl;
    }

    curl_multi_cleanup(multi_handle);
    for(int i = 0; i < files_count; i++) {
        curl_easy_cleanup(handles[i]);
    }

    return 0;
}

