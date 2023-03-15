def predict_gen(meta1):
    import pickle
    import numpy as np
    import os
    from django.conf import settings
    path = os.path.join(settings.MODELS, 'baby_cry_classification_model_final.pkl')
 
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    d1 =np.array(meta1)
   

    with open(path,'rb') as pickled:
        model = pickle.load(pickled)
    
    svmp=model['svmp']
    norma=model['norma']
    lcn=model['lgn']

    data1=norma.transform([meta1])

    predicted_genre = svmp.predict(data1)
    print(predicted_genre[0])
    return predicted_genre[0]
   