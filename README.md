# face-detection
The program detects how many faces are in a given picture. It prints an integer and shows the chosen image with each face outlined. 

# To run: \
-must have the haar_cascade file in the same directory. This contains around 6000 patterns for the program to read and recognize as patterns found in a face. \
-must also have your test photo in the same directory. \
-the filepath for both of these files must be included in the program. If using Google Colab and uploading the files into colab directly, the filepath with be /content/filename 

cv2_imshow is a Google Colab patch for the original function from cv2 library which was cv2.imshow(). If you are not using Colab, comment out this import and change that line back to .imshow(). There was just some incompatibility between Colab and cv2 for that function.

