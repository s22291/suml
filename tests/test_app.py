from app.predict import predict

def test_predict_returns_valid_class():
    fake_input = {
        'N_Days': 0,
        'Age': 50,
        'Stage': 2,
        'Platelets': 200,
        'Bilirubin': 1.0,
        'Cholesterol': 200.0,
        'Albumin': 3.5,
        'Copper': 50.0,
        'Alk_Phos': 100.0,
        'SGOT': 30.0,
        'Tryglicerides': 120.0,
        'Prothrombin': 10.0,
        'Drug_Placebo': 0,
        'Sex_M': 1,
        'Ascites_Y': 0,
        'Hepatomegaly_Y': 0,
        'Spiders_Y': 1,
        'Edema_S': 0,
        'Edema_Y': 0
    }

    result = predict(fake_input)
    assert result in [0, 1]
