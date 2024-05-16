import qrcode
import cv2

 # Encoding text (data) and saving it into named file to generate QRcode.
def QRcodeGenerate(data, file):
    image = qrcode.make(data)
    image.save(file)

# Decoding the QR code image from the specified file name.
def decodeQRcode(filename):
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, points, straight_qrcode = detector.detectAndDecode(image)
    return data

# The main is where to excute the program and where the user inputs.
def main():
    data = input("Enter the data to encode: ")
    filename = input("Enter the filename to save the QR code (example: code.png): ")

    QRcodeGenerate(data, filename)
    print("QR code generated successfully!")

    dataDecode = decodeQRcode(filename)
    print("Decoded data from QR code:", dataDecode)

#Execute program as long as it is in the main() function.
if __name__ == "__main__":
    main()
