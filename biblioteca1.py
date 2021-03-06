import numpy as np
import re 
from tensorflow.keras.utils import to_categorical
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt

class wordcloud1():

    def __init__(self, data, language = 'english', encod = 'latin-1'):
        self.data = data
        self.language = language
        
    def graph(self):
        if self.language.lower() in ['english','ingles']:
            stopwords = set(STOPWORDS)
            stopwords.update(['i','me','my','myself','we','our','ours','ourselves','you','your',
                              'yours','yourself','yourselves','he','him','his','himself','she',
                              'her','hers','herself','it','its','itself','they','them','their','theirs',
                              'themselves','what','which','who','whom','this','that','these','those',
                              'am','is','are','was','were','be','been','being','have','has','had','having',
                              'do','does','did','doing','a','an','the','and','but','if','or','because','as',
                              'until','while','of','at','by','for','with','about','against','between','into',
                              'through','during','before','after','above','below','to','from','up','down','in',
                              'out','on','off','over','under','again','further','then','once','here','there','when',
                              'where','why','how','all','any','both','each','few','more','most','other','some','such',
                              'no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just',
                              'don','should','now'])
            wordcloud = WordCloud(stopwords = stopwords, background_color='black', width= 3200, height=1600).generate(self.data)
        if self.language.lower() in ['portuguese', 'portugues']:
            stopwords = set(STOPWORDS)
            stopwords.update(['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', '??', 'com', 'n??o',
                              'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi',
                              'ao', 'ele', 'das', 'tem', '??', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'h??',
                              'nos', 'j??', 'est??', 'eu', 'tamb??m', 's??', 'pelo', 'pela', 'at??', 'isso', 'ela',
                              'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me',
                              'esse', 'eles', 'est??o', 'voc??', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu',
                              '??s', 'minha', 't??m', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'ser??', 'n??s',
                              'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te',
                              'voc??s', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa',
                              'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles',
                              'aquelas', 'isto', 'aquilo', 'estou', 'est??', 'estamos', 'est??o', 'estive', 'esteve', 'estivemos',
                              'estiveram', 'estava', 'est??vamos', 'estavam', 'estivera', 'estiv??ramos', 'esteja', 'estejamos', 
                              'estejam', 'estivesse', 'estiv??ssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei',
                              'h??', 'havemos', 'h??o', 'houve', 'houvemos', 'houveram', 'houvera', 'houv??ramos', 'haja', 'hajamos',
                              'hajam', 'houvesse', 'houv??ssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 
                              'houver??', 'houveremos', 'houver??o', 'houveria', 'houver??amos', 'houveriam', 'sou', 'somos', 's??o',
                              'era', '??ramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'f??ramos', 'seja',  'sejamos',
                              'sejam', 'fosse', 'f??ssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'ser??', 'seremos', 'ser??o',
                              'seria', 'ser??amos', 'seriam', 'tenho', 'tem', 'temos', 't??m', 'tinha', 't??nhamos', 'tinham', 'tive', 'teve',
                              'tivemos', 'tiveram', 'tivera', 'tiv??ramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tiv??ssemos', 'tivessem',
                              'tiver', 'tivermos', 'tiverem', 'terei', 'ter??', 'teremos', 'ter??o', 'teria', 'ter??amos', 'teriam'])
            
            wordcloud = WordCloud(stopwords = stopwords, background_color='black', width= 3200, height=1600).generate(self.data)

        return wordcloud.to_file('tmp/wordcloud.png')
