from sklearn.metrics import confusion_matrix
actual = [0, 1, 0, 1]
predicted = [1, 1, 1, 0]
cm = confusion_matrix(actual, predicted)
print(type(cm))
print(" ", "0 ", "1 ", "P ")
print(0, "TN", "FP")
print(1, "FN", "TP")
print("A")
print()
print("confusion matrix")
print(cm)
# ravel - returns a flattened array in row major style
r = cm.ravel()
print(type(r))
tn, fp, fn, tp = cm.ravel()
print("TN", tn, "FP", fp, "FN", fn, "TP", tp)

from sklearn.metrics import confusion_matrix
actual = ['B', 'M', 'B', 'M']
predicted = ['M', 'M', 'M', 'B']
# in aphabetical order, B is 0, M is 1
cm = confusion_matrix(actual, predicted)
print(" ", "B ", "M ", "P ")
print("B", "TN", "FP")
print("M", "FN", "TP")
print("A")
print()
print("CM", cm)
print()

from sklearn.metrics import confusion_matrix
actual = ['W', 'M', 'W', 'M']
predicted = ['M', 'M', 'M', 'W']
# labels forces W to 0 (negative) and M to 1 (positive)
cm = confusion_matrix(actual, predicted, labels=["W", "M"])
print(" ", "W ", "M ", "P ")
print("W ", "TN", "FP")
print("M ", "FN", "TP")
print("A")
print()
print("CM", cm)

actual = ["cat", "ant", "cat", "cat", "ant", "bird"]
predicted = ["ant", "ant", "cat", "cat", "ant", "cat"]
cm = confusion_matrix(actual, predicted)
print(cm)
cm = confusion_matrix(actual, predicted,labels=["ant", "cat", "bird"])
print(cm)