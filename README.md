# chatbot
Bu proje basit bir Chatbot projesidir. Projenin gelişimine katkı sağlayabilir veya klonlayabilirsiniz. Kurulum adımlarını takip ederek kolayca çalıştırabilirsiniz. 

intents.txt dosyası chatbot'un veritabanı intents.json dosyasını hazırlamayı kolaylaştırmak için. Örnekteki gibi bir intents.txt dosyasını cep telefonunuzda bir not defterinde oluşturabilirsiniz.

K: (intensts.json dosyasında tag
U: (intensts.json dosyasında patterns)
A: (intensts.json dosyasında responses)'i ı temsil eder.)

Tercihen conda ile bir sanal alan oluşturabilirsiniz:.
conda create -n chatbot python=3.8
conda activate chatbot

https://github.com/matrixportal/chatbot.git
cd chatbot
python train.py

Chatbotla komut satırında sohbet etmek için aşağıdaki komutu kullanabilirsiniz:
python chatbot.py

Chatbotla web sayfasından sohbet etmek için aşağıdaki nodejs komutlarını kullanabilirsiniz:
npm i
node chatbot.js

Chatbotla sohbete başlamak için aşağıdaki adresi tarayıcıda açın:
http://localhost:5000/

re
numpy-1.24.3
torch-2.0.1
nltk-3.8.1
requests-2.30.0
pytz-2023.3
