# Canny con diferentes umbrales

canny_1 = cv2.Canny(imagen, 10, 50)
canny_2 = cv2.Canny(imagen, 50, 150)
canny_3 = cv2.Canny(imagen, 100, 200)
canny_4 = cv2.Canny(imagen, 200, 250)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(canny_1, cmap='gray')
plt.title('Canny: 10 - 50')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(canny_2, cmap='gray')
plt.title('Canny: 50 - 150')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(canny_3, cmap='gray')
plt.title('Canny: 100 - 200')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(canny_4, cmap='gray')
plt.title('Canny: 200 - 250')
plt.axis('off')

plt.tight_layout()
plt.show()