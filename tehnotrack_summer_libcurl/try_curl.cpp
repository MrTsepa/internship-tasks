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
    if (argc != 2) {
        std::cout << "Usage my_curl <url>" << std::endl;
        return 0;
    }
    std::cout << "Downloading from " << argv[1] << std::endl;
    CURL *handle = curl_easy_init();
    CURLM *multi_handle = curl_multi_init();
    curl_easy_setopt(handle, CURLOPT_URL, argv[1]);
    curl_easy_setopt(handle, CURLOPT_WRITEFUNCTION, write_data);
    curl_multi_add_handle(multi_handle, handle);

    int running_handles;
    curl_multi_perform(multi_handle, &running_handles);
    while(running_handles == 1) {
        curl_multi_perform(multi_handle, &running_handles);
        double size_downloaded;
        double content_length;
        curl_easy_getinfo(handle, CURLINFO_CONTENT_LENGTH_DOWNLOAD, &content_length);
        curl_easy_getinfo(handle, CURLINFO_SIZE_DOWNLOAD, &size_downloaded);
        if (size_downloaded > 0) {
            std::cout << "Downloading... " << std::setprecision(2) << size_downloaded / content_length * 100 << "%... " <<  std::setprecision(10) << size_downloaded << " bytes of " << content_length << std::endl;
        } else {
            std::cout << "Connecting..." << std::endl;
        }
        usleep(1000000);
    }
    std::cout << std::endl;

    double size_download;
    double speed;
    curl_easy_getinfo(handle, CURLINFO_SIZE_DOWNLOAD, &size_download);
    curl_easy_getinfo(handle, CURLINFO_SPEED_DOWNLOAD, &speed);
    std::cout << "Downloaded " << size_download << " bytes at speed " << speed << " bytes/sec." << std::endl;

    curl_multi_cleanup(multi_handle);
    curl_easy_cleanup(handle);

  return 0;
}
