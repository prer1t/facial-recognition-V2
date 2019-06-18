faces,Ids = getImagesAndLabels('dataSet/')
recognizer.train(faces, np.array(Ids))
recognizer.save('training/Recogniser.yml')

print('training complete')
