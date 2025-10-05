from transformers import AutoTokenizer, AutoModelForCausalLM

# Modelo compatible con versiones antiguas
model_name = "distilgpt2"

# Cargar tokenizer y modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Texto de entrada
input_text = "Hi, tell me something about the apollo mission 17"

# Tokenizar
inputs = tokenizer(input_text, return_tensors="pt")

# Generar texto
outputs = model.generate(**inputs, max_length=2000,
    do_sample=True,       # para que sea más creativo
    top_k=50,             # limitar opciones por token
    top_p=0.95,           # muestreo de núcleo
    temperature=0.7)

# Mostrar resultado
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
