import requests
from openai import OpenAI, APIConnectionError



class Processing:
    client = OpenAI(api_key= "")
    def __init__(self):
        pass

    def setApiKey(self, api_key):
        self.client = OpenAI(api_key= api_key)

    def openai_translate(self, text):
        try:
            response = self.client.chat.completions.create(
              model="gpt-3.5-turbo-0125",
              messages=[
                {
                  "role": "system",
                  "content": [
                    {
                      "text": "Tu es un traducteur, tu traduis des textes dans les 4 langues suivantes : francais, anglais, allemand et espagnol.",
                      "type": "text"
                    }
                  ]
                },
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "Traduit : Bonjour tout le monde !"
                    }
                  ]
                },
                {
                  "role": "assistant",
                  "content": [
                    {
                      "text": "{\n  \"francais\": \"Bonjour tout le monde !\",\n  \"anglais\": \"Hello everyone!\",\n  \"allemand\": \"Hallo zusammen!\",\n  \"espagnol\": \"¡Hola a todos!\"\n}",
                      "type": "text"
                    }
                  ]
                },
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "My name is Christopher"
                    }
                  ]
                },
                {
                  "role": "assistant",
                  "content": [
                    {
                      "text": "{\n  \"francais\": \"Mon nom est Christopher\",\n  \"anglais\": \"My name is Christopher\",\n  \"allemand\": \"Mein Name ist Christopher\",\n  \"espagnol\": \"Mi nombre es Christopher\"\n}",
                      "type": "text"
                    }
                  ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "text": text,
                            "type": "text"
                        }
                      ]
                  }
              ],
              temperature=1,
              max_tokens=2048,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0,
              response_format={
                "type": "text"
              }
            ).choices[0].message.content
        except APIConnectionError as e:
            response = "Error: API connection error. Please check your API key and try again."

        return response

    def openai_summarize(self, text):
        try:
            response = self.client.chat.completions.create(
                  model="gpt-3.5-turbo-0125",
                  messages=[
                    {
                      "role": "system",
                      "content": [
                        {
                          "type": "text",
                          "text": "Résume le texte en quelques phrases, 10 phrases max.\n"
                        }
                      ]
                    },
                    {
                      "role": "user",
                      "content": [
                        {
                          "type": "text",
                          "text": "Son nom est GS0023054. C'est le nom qu'il a reçu quand il a été affecté à cette mission. Pour un IGAM, c'est la tradition. Le G signifie qu'il est un gardien, et le S qu'il est affecté à un système solaire. Quant au numéro, il n'est pas important de s’appesantir dessus, il n'a de signification que pour les IGAMS. Ce n'est en aucun cas un numéro, ni une identification. Les IGAMS n'ont aucune notion d'individualité. Les IGAMS sont des êtres immatériels. Leur existence n'est pas liée aux contraintes de l'univers dans lequel ils évoluent. Ils sont immortels, pour autant que ce terme est un sens pour eux, ils ne sont pas nés, n'ont pas de liens particuliers avec le passé ou le futur. Ils existent tout simplement. Chaque individu est relié à la communauté par des liens télépathiques. GS0023054 est affecté à la surveillance d'un système solaire sur lequel la communauté des IGAMS a implanté une forme de vie. Son objectif est de vérifier que tout se passe comme convenu, mais sans jamais intervenir, ce n'est pas son rôle, il agit un peu comme une balise, comme un témoin. Il est là, le temps qu'il faut, jusqu'à ce que le développement soit arrivé à son terme, et que la « Mère » vienne récolter le fruit de ce développement. Le système qu'il a en charge est appelé « Soleil », et la planète sur laquelle l’implantation a eu lieu, « la Terre ». C'est la troisième fois que les IGAMS font une implantation sur cette planète , et ce sera la dernière. Les deux expériences précédentes se sont soldées par des échecs, et la « Mère » a décidé que ce serait la dernière. La précédente implantation a eu lieu il y a 230 millions d'années, et la race des reptiles, n'a pas pu aller au terme de son développement. Les IGAMS, au bout de 165 millions d'années, ont jugé que cette race ne répondait pas à leurs espoirs, et ont donc décidé de stopper cette expérience. Ils les ont éliminés pour faire place à une nouvelle implantation, celle qui est en cours actuellement. Les IGAMS colonisent de cette façon une grande partie de l'univers, celui que l'on voit, et tous les autres. Il y a une infinité d'implantations de ce type, et quand cela se solde par un échec, ils n'en ressentent aucune amertume, ni aucune émotion. Ce sont des êtres qui ne connaissent pas les notions de sentiments et d'individualisme. Ils ne sont pas nés, ne mourront jamais, et ne sont pas dépendants des aléas d'un corps physique. Malgré tout, ils ont besoin d’énergie et d'influx télépathiques. C'est pour cela qu'ils implantent des colonies sur des planètes. Ils ont besoin que ces colonies développent un réseau d'intelligence, principalement des pensées et des concepts. C'est ce qui n'a pas fonctionné avec la dernière implantation sur la terre. Les dinosaures n’émettaient aucune pensée cohérente, seulement des besoins basiques comme la faim, la soif ou le désir de reproduction. Rien d'intéressant, car ces pulsions avaient été programmées par les IGAMS lors de l'implantation de cette race. Sur la terre, il y a maintenant plusieurs millénaires, les IGAMS ont implanté une espèce plus évoluée dont ils espèrent beaucoup. « Les humains », car c'est de cette espèce qu'il s'agit, ont donné de bons résultats sur les planètes des galaxies Andromède et Triangle, où elles ont été implantées. La « Mère », a déjà fait plusieurs récoltes dans ces galaxies, principalement des ensembles de concepts reliés par un réseau de pensées télépathiques. C'est ce que GS attend de voir se produire sur la terre."
                        }
                      ]
                    },
                    {
                      "role": "assistant",
                      "content": [
                        {
                          "type": "text",
                          "text": "GS0023054 est un gardien IGAM immatériel chargé de surveiller la Terre, où une nouvelle implantation de vie est en cours. Son rôle est d'observer sans intervenir, agissant comme une balise pour la communauté IGAM. Les IGAMS sont des êtres immortels, dépourvus de sentiment ou d'individualité. Ils colonisent diverses planètes pour récolter de l'énergie et des influx télépathiques, cherchant des pensées cohérentes et des concepts évolués. Les dinosaures précédemment implantés sur Terre ont été éliminés pour échec de développement après 165 millions d'années. Les humains, implantés il y a plusieurs millénaires, offrent de bons résultats ailleurs et sont l'espoir des IGAMS pour la Terre. La \"Mère\" viendra récolter ces concepts télépathiques une fois le développement abouti."
                        }
                      ]
                    },
                    {
                      "role": "user",
                      "content": [
                        {
                          "type": "text",
                          "text":  text
                        }
                      ]
                    }
                  ],
                  temperature=1,
                  max_tokens=2048,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0,
                  response_format={
                    "type": "text"
                  }
                ).choices[0].message.content
        except APIConnectionError as e:
            response = "Error: API connection error. Please check your API key and try again."

        return response

    def openai_generate(self, text):
        try:
            response = self.client.chat.completions.create(
                  model="gpt-3.5-turbo-0125",
                  messages=[
                    {
                      "role": "system",
                      "content": [
                        {
                          "type": "text",
                          "text": "Rédige du contenus en rapport avec la thématique donnée, 500 mots max.\n"
                        }
                      ]
                    },
                    {
                      "role": "user",
                      "content": [
                        {
                          "type": "text",
                          "text": "Redige moi un texte en rapport avec l'IA"
                        }
                      ]
                    },
                    {
                      "role": "assistant",
                      "content": [
                        {
                          "type": "text",
                          "text": "L'intelligence artificielle, communément désignée par le sigle IA, est un domaine en plein essor qui suscite un intérêt grandissant dans de nombreux secteurs d'activité. Elle englobe un ensemble de technologies permettant aux machines d'imiter l'intelligence humaine pour effectuer des tâches variées, allant de la reconnaissance vocale à la prise de décisions complexes.\n\nLes progrès rapides réalisés ces dernières années dans le domaine de l'IA ont permis le développement de nombreux outils et applications révolutionnaires. Par exemple, l'IA est utilisée dans les systèmes de recommandation des plateformes de streaming, les assistants personnels virtuels comme Siri ou Alexa, ou encore les véhicules autonomes.\n\nLes algorithmes d'apprentissage automatique, et en particulier le deep learning, ont permis d'énormes avancées en matière de reconnaissance d'images, de traitement du langage naturel et de prédiction. Les possibilités offertes par l'IA sont infinies et ont un potentiel transformateur dans de nombreux domaines.\n\nCependant, l'IA soulève également des questions éthiques et sociétales importantes. Par exemple, la question de la responsabilité en cas de décisions prises par des machines autonomes, ou encore celle de la protection des données personnelles dans un monde de plus en plus connecté.\n\nDe plus, l'IA peut également poser des défis en matière d'emploi, certains craignant que l'automatisation de nombreuses tâches ne conduise à une perte massive d'emplois dans certains secteurs. Il est donc essentiel de réfléchir à la manière dont l'IA peut être utilisée de manière éthique et responsable pour garantir des bénéfices pour l'ensemble de la société.\n\nMalgré ces enjeux, l'IA offre de nombreuses opportunités pour améliorer notre quotidien, que ce soit en optimisant nos processus de travail, en nous assistant dans nos prises de décision ou en nous proposant des expériences personnalisées et adaptées à nos besoins.\n\nEn conclusion, l'intelligence artificielle est un domaine en constante évolution qui promet de révolutionner de nombreux aspects de nos vies. Il est essentiel de promouvoir une utilisation éthique et responsable de ces technologies innovantes afin de garantir des bénéfices durables pour tous."
                        }
                      ]
                    },
                    {
                      "role": "user",
                      "content": [
                        {
                          "type": "text",
                          "text": text
                        }
                      ]
                    },
                  ],
                  temperature=1,
                  max_tokens=2048,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0,
                  response_format={
                    "type": "text"
                  }
                ).choices[0].message.content
        except APIConnectionError as e:
            response = "Error: API connection error. Please check your API key and try again."

        return response

    def openai_codex(self, text):
        try:
            response = self.client.chat.completions.create(
              model="gpt-3.5-turbo-0125",
              messages=[
                {
                  "role": "system",
                  "content": [
                    {
                      "type": "text",
                      "text": "Corrige les erreurs dans le code.\nTu peux corriger tout les langages. \nMet un commentaire sur la ligne qui présente une erreur pour l'indiquer.\n"
                    }
                  ]
                },
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "import os\r\nfrom openai import OpenAI\r\n\r\nclient = OpenAI(\r\n    #Placer votre clé API dans la variable ci-dessous\r\n    api_key=\"YOUR_API_KEY\",\r\n)\r\n\r\nchat_completion = client.chat.completions.create(\r\n    messages=[\r\n         {\r\n             \"role\": \"system\",\r\n         \"content\": f\"Tu es un rédacteur web qui synthétise l'actualité en 50 mots sur la thématique 'IA' Tu fais des liaisons entre les articles avec des mots tel que 'mais', 'donc', 'or', 'par contre', 'en revanche', 'en effet', 'cependant', 'toutefois', 'par ailleurs', 'par contre', 'par contre, 'enfin'\"\r\n         },\r\n\r\n        {\r\n            \"role\": \"user\",\r\n            \"content\": \"Say this is a test\",\r\n        }\r\n    ]\r\n    model=\"gpt-3.5-turbo\",\r\n    temperature=0.3,\r\n  max_tokens=100,\r\n  top_p=1.0,\r\n  frequency_penalty=0.0,\r\n  presence_penalty=0.0\r\n)"
                    }
                  ]
                },
                {
                  "role": "assistant",
                  "content": [
                    {
                      "type": "text",
                      "text": "```python\nfrom openai import OpenAI  # Erreur: Le module 'openai' n'est pas importé correctement\n\nclient = OpenAI(\n    # Placer votre clé API dans la variable ci-dessous\n    api_key=\"YOUR_API_KEY\",\n)\n\nchat_completion = client.chat.completions.create(\n    messages=[\n         {\n             \"role\": \"system\",\n             \"content\": f\"Tu es un rédacteur web qui synthétise l'actualité en 50 mots sur la thématique 'IA'. Tu fais des liaisons entre les articles avec des mots tels que 'mais', 'donc', 'or', 'par contre', 'en revanche', 'en effet', 'cependant', 'toutefois', 'par ailleurs', 'par contre', 'par contre', 'enfin'\"  # Erreur: Il manque un guillemet simple à la fin de la chaîne de caractères\n         },\n\n        {\n            \"role\": \"user\",\n            \"content\": \"Say this is a test\",\n        }\n    ],  # Erreur: Il manque une virgule à la fin de cette ligne\n\n    model=\"gpt-3.5-turbo\",\n    temperature=0.3,\n    max_tokens=100,\n    top_p=1.0,\n    frequency_penalty=0.0,\n    presence_penalty=0.0\n)\n```"
                    }
                  ]
                },
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "class MisspelledVar {\n    public static void main(String args[])\n    {\n        int a = 40, b = 60;\n\n        // Declared variable Sum with Capital S\n        int Sum = a + b;\n\n        // Trying to call variable Sum\n        // with a small s ie. sum\n        System.out.println(\n            \"Sum of variables is \"\n            + sum);\n    }\n}\n"
                    }
                  ]
                },
                {
                  "role": "assistant",
                  "content": [
                    {
                      "type": "text",
                      "text": "```java\nclass MisspelledVar {\n    public static void main(String args[]) {\n        int a = 40, b = 60;\n\n        // Declared variable Sum with Capital S\n        int Sum = a + b;\n\n        // Trying to call variable Sum\n        // with a small s ie. sum\n        System.out.println(\"Sum of variables is \" + Sum);\n    }\n}\n```"
                    }
                  ]
                },
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": text
                    }
                  ]
                },
              ],
              temperature=1,
              max_tokens=2048,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0,
              response_format={
                "type": "text"
              }
            ).choices[0].message.content
        except APIConnectionError as e:
            response = "Error: API connection error. Please check your API key and try again."

        return response

    def openai_create_image(self, prompt):
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            ).data[0].url

        except APIConnectionError as e:
            response = "Error: API connection error. Please check your API key and try again."
        return response

    def openai_create_image_variation(self, img):
        response = self.client.images.create_variation(
            model="dall-e-2",
            image=open(img, "rb"),
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return image_url
