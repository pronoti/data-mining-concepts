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


actual = ["cat", "ant", "cat", "cat", "ant", "bird"]
predicted = ["ant", "ant", "cat", "cat", "ant", "cat"]
cm = confusion_matrix(actual, predicted)
print(cm)
cm = confusion_matrix(actual, predicted,
labels=["ant", "cat", "bird"])
print(cm)