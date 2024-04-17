from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('startup (1).pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
    s1= request.form["symptom1"]
    s2= request.form["symptom2"]
    s3= request.form["symptom3"]
    s4= request.form["symptom4"]
    s5= request.form["symptom5"]
    s6= request.form["symptom6"]
    s7= request.form["symptom7"]
    s8= request.form["symptom8"]
    s9= request.form["symptom9"]
    s10= request.form["symptom10"]
    s11= request.form["symptom11"]
    s12= request.form["symptom12"]
    s13= request.form["symptom13"]
    s14= request.form["symptom14"]
    s15= request.form["symptom15"]
    s16= request.form["symptom16"]
    s17= request.form["symptom17"]


    d={
        "itching":1,
        "skin_rash":3,
        "nodal_skin_eruptions":4,
        "continuous_sneezing":4,
        "shivering":5,
        "chills":3,
        "joint_pain":3,
        "stomach_pain":	5,
        "acidity":3,
        "ulcers_on_tongue":4,
        "muscle_wasting":3,
        "vomiting":5,
        "burning_micturition":6,
        "spotting_urination":6,
        "fatigue":4,
        "weight_gain":3,
        "anxiety":4,
        "cold_hands_and_feets":5,
        "mood_swings":3,
        "weight_loss":3,
        "restlessness":5,
        "lethargy":2,
        "patches_in_throat":6,
        "irregular_sugar_level":5,
        "cough":4,
        "high_fever":7,
        "sunken_eyes":3,
        "breathlessness":4,
        "sweating":3,
        "dehydration":4,
        "indigestion":5,
        "headache":3,
        "yellowish_skin":3,
        "dark_urine":4,
        "nausea":5,
        "loss_of_appetite":4,
        "pain_behind_the_eyes":4,
        "back_pain":3,
        "constipation":4,
        "abdominal_pain":4,
        "diarrhoea":6,
        "mild_fever":5,
        "yellow_urine":4,
        "yellowing_of_eyes":4,
        "acute_liver_failure":6,
        "fluid_overload":6,
        "swelling_of_stomach":7,
        "swelled_lymph_nodes":6,
        "malaise":6,
        "blurred_and_distorted_vision":5,
        "phlegm":5,
        "throat_irritation":4,
        "redness_of_eyes":5,
        "sinus_pressure":4,
        "runny_nose":5,
        "congestion":5,
        "chest_pain":7,
        "weakness_in_limbs":7,
        "fast_heart_rate":5,
        "pain_during_bowel_movements":5,
        "pain_in_anal_region":6,
        "bloody_stool":5,
        "irritation_in_anus":6,
        "neck_pain":5,
        "dizziness":4,
        "cramps":4,
        "bruising":4,
        "obesity":4,
        "swollen_legs":5,
        "swollen_blood_vessels":5,
        "puffy_face_and_eyes":5,
        "enlarged_thyroid":6,
        "brittle_nails":5,
        "swollen_extremeties":5,
        "excessive_hunger":4,
        "extra_marital_contacts,":5,
        "drying_and_tingling_lips":4,
        "slurred_speech":4,
        "knee_pain":3,
        "hip_joint_pain":2,
        "muscle_weakness":2,
        "stiff_neck":4,
        "swelling_joints":5,
        "movement_stiffness":5,
        "spinning_movements":6,
        "loss_of_balance":4,
        "unsteadiness":	4,
        "weakness_of_one_body_side":	4,
        "loss_of_smell":	3,
        "bladder_discomfort":	4,
        "foul_smell_ofurine":	5,
        "continuous_feel_of_urine":	6,
        "passage_of_gases":	5,
        "internal_itching":	4,
        "toxic_look_(typhos)":	5,
        "depression":	3,
        "irritability":	2,
        "muscle_pain":	2,
        "altered_sensorium":	2,
        "red_spots_over_body":	3,
        "belly_pain":	4,
        "abnormal_menstruation":	6,
        "dischromic_patches":	6,
        "watering_from_eyes":	4,
        "increased_appetite":	5,
        "polyuria":	4,
        "family_history":	5,
        "mucoid_sputum":	4,
        "rusty_sputum":	4,
        "lack_of_concentration":	3,
        "visual_disturbances":	3,
        "receiving_blood_transfusion":	5,
        "receiving_unsterile_injections":	2,
        "coma":	7,
        "stomach_bleeding":	6,
        "distention_of_abdomen":	4,
        "history_of_alcohol_consumption":	5,
        "fluid_overload":	4,
        "blood_in_sputum":	5,
        "prominent_veins_on_calf":	6,
        "palpitations":	4,
        "painful_walking":	2,
        "pus_filled_pimples":	2,
        "blackheads":	2,
        "scurring":	2,
        "skin_peeling":	3,
        "silver_like_dusting":	2,
        "small_dents_in_nails":	2,
        "inflammatory_nails":	2,
        "blister":	4,
        "red_sore_around_nose":	2,
        "yellow_crust_ooze":	3,
        "prognosis":	5,
        "":0.0
}
    
    t = [[float(d[s1]),float(d[s2]),float(d[s3]),float(d[s4]),float(d[s5]),float(d[s6]),float(d[s7]),float(d[s8]),float(d[s9]),float(d[s10]),float(d[s11]),float(d[s12]),float(d[s13]),float(d[s14]),float(d[s15]),float(d[s16]),float(d[s17])]]
    output =model.predict(t)
    d1={
        "Drug Reaction": ["stop irritation","consult nearest hospital","stop taking drug","follow up"],
        "Malaria": ["Consult nearest hospital",	"avoid oily food","avoid non veg food","keep mosquitos out"],
        "Allergy": ["apply calamine","cover area with bandage","use ice to compress itching", " "],
        "Hypothyroidism": ["reduce stress"	,"exercise",	"eat healthy"	,"get proper sleep"],
        "Psoriasis": ["wash hands with warm soapy water",	"stop bleeding using pressure",	"consult doctor",	"salt baths"],
        "GERD": ["avoid fatty spicy food"	,"avoid lying down after eating",	"maintain healthy weight"	,"exercise"],
        "Chronic cholestasis": ["cold baths",	"anti itch medicine",	"consult doctor",	"eat healthy"],
        "hepatitis A": ["Consult nearest hospital",	"wash hands through",	"avoid fatty spicy food",	"medication"],
        "Osteoarthristis": ["acetaminophen",	"consult nearest hospital",	"follow up",	"salt baths"],
        "(vertigo) Paroymsal":  ["Positional Vertigo	lie down",	"avoid sudden change in body",	"avoid abrupt head movment",	"relax"],
        "Hypoglycemia": ["lie down on side",	"check in pulse",	"drink sugary drinks",	"consult doctor"],
        "Acne": ["bath twice",	"avoid fatty spicy food",	"drink plenty of water",	"avoid too many products"],
        "Diabetes ": ["have balanced diet",	"exercise",	"consult doctor",	"follow up"],
        "Impetigo": ["soak affected area in warm water"	,"use antibiotics",	"remove scabs with wet compressed cloth",	"consult doctor"],
        "Hypertension":  ["meditation",	"salt baths",	"reduce stress",	"get proper sleep"],
        "Peptic ulcer diseae": ["avoid fatty spicy food",	"consume probiotic food",	"eliminate milk"	,"limit alcohol"],
        "Dimorphic hemmorhoids(piles)": ["avoid fatty spicy food",	"consume witch hazel"	,"warm bath with epsom salt"	,"consume alovera juice"],
        "Common Cold": ["drink vitamin c rich drinks",	"take vapour",	"avoid cold food",	"keep fever in check"],
        "Chicken pox": ["use neem in bathing", 	"consume neem leaves",	"take vaccine",	"avoid public places"],
        "Cervical spondylosis": ["use heating pad or cold pack"	,"exercise",	"take otc pain reliver",	"consult doctor"],
        "Hyperthyroidism": ["eat healthy"	,"massage"	,"use lemon balm"	,"take radioactive iodine treatment"],
        "Urinary tract infection": ["drink plenty of water",	"increase vitamin c intake",	"drink cranberry juice",	"take probiotics"],
        "Varicose": ["veins	lie down flat and raise the leg high"	,"use oinments",	"use vein compression",	"dont stand still for long"],
        "AIDS": ["avoid open cuts",	"wear ppe if possible",	"consult doctor",	"follow up"],
        "Paralysis (brain hemorrhage)": ["massage",	"eat healthy",	"exercise",	"consult doctor"],
        "Typhoid": ["eat high calorie vegitables",	"antiboitic therapy",	"consult doctor",	"medication"],
        "Hepatitis B": ["consult nearest hospital",	"vaccination",	"eat healthy",	"medication"],
        "Fungal infection": ["bath twice",	"use detol or neem in bathing water",	"keep infected area dry",	"use clean cloths"],
        "Hepatitis C": ["Consult nearest hospital",	"vaccination",	"eat healthy",	"medication"],
        "Migraine": ["meditation",	"reduce stress",	"use poloroid glasses in sun",	"consult doctor"],
        "Bronchial": ["Asthma",	"switch to loose cloothing",	"take deep breaths",	"get away from trigger"	"seek help"],
        "Alcoholic": ["hepatitis	stop alcohol consumption",	"consult doctor",	"medication",	"follow up"],
        "Jaundice": ["drink plenty of water",	"consume milk thistle",	"eat fruits and high fiberous food",	"medication"],
        "Hepatitis E": ["stop alcohol consumption",	"rest",	"consult doctor",	"medication"],
        "Dengue": ["drink papaya leaf juice",	"avoid fatty spicy food",	"keep mosquitos away",	"keep hydrated"],
        "Hepatitis D": ["consult doctor"	,"medication",	"eat healthy",	"follow up"],
        "Heart attack": ["call ambulance",	"chew or swallow asprin"	,"keep calm"," "	],
        "Pneumonia": ["consult doctor"	,"medication"	,"rest"	,"follow up"],
        "Arthritis": ["exercise",	"use hot and cold therapy",	"try acupuncture",	"massage"],
        "Gastroenteritis": ["stop eating solid food for while"	,"try taking small sips of water",	"rest"	,"ease back into eating"],
        "Tuberculosis": ["cover mouth"	,"consult doctor",	"medication",	"rest"]

    }

   
    h = "Disease: " + output[0] 
    a="  precaution-1: " + d1[output[0]][0] 
    b= "  precaution2: " + d1[output[0]][1] 
    c= "  precaution3: " + d1[output[0]][2] 
    d="  precaution4: " + d1[output[0]][2]

  
    return render_template("index.html", v = str((h)),w = str((a)),x = str((b)),y = str((c)),z = str((d)))


if __name__ == '__main__' :
    app.run(debug=True) 
          
