import speedtest
import converter

def main() -> None:

    test = speedtest.Speedtest()

    #download
    print("Testando download")
    speed_download = converter.bytes_to_mb(test.download())

    #upload
    print("Testando upload")
    speed_upload = converter.bytes_to_mb(test.upload())

    print(f"A velocidade de download: {speed_download} Megabyte(s)")
    print(f"A velocidade upload: {speed_upload} Megabyte(s)")

if __name__ == '__main__':
    main()