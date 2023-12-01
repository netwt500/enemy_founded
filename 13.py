import cv2

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_default.xml')

img = cv2.imread('./image/cats.jpg')
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cats = cat_cascade.detectMultiScale(g, 1.01, 4,minSize=(200,200))

for (x, y, w, h) in cats:
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

print('Number of cats =', len(cats))

cv2.imshow('img', img)
cv2.waitKey(0)

