# YOUR OWN SPHERE

If you need to create your own Sphere, maybe with swearing or humorer answers, this documentation was created just for you

After creating of resource-pack you need to change value of variable in the "src/\_\_main\_\_.py" file in line " resource_pack = 'resource-pack name' "

# Resource-pack Structure

Your resource-pack must include this files:

1. Language("/langs/language.json"): main Sphere actions writes right here
2. Answer("/langs/answer_files/answers_язык.json"): Sphere's dictionary for Sphere's reactions writes right here

# Language File

For now this file has so pure settings but included settings are:

1. "lang": language of file
2. "text": displayed text settings:
    1. "init_text": text writes when model starts
    2. "answer_formatting": text formatting that must have an "{answer}" for answer and "{question}" for user question
    3. "type_text": question input text
    4. "model_text": text formatting of Model
    5. "custom_model_text": text formatting for choosing model seed
    6. "stop_words": list of words for Sphere stopping

# Answer file

In this file logically too many different settings... groups:

1. "lang": language of file
2. "answers": list of answer groups

    "test answer group": answer group

        1. "masks": word or phrase for determination of current group(first mask should be "#group_name")
        2. "answers": answers for group questions

# And keep in mind

If you don't understood you need just send me your problem
