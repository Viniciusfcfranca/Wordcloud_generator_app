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
            stopwords.update(['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não',
                              'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi',
                              'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há',
                              'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela',
                              'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me',
                              'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu',
                              'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós',
                              'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te',
                              'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa',
                              'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles',
                              'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos',
                              'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 
                              'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei',
                              'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos',
                              'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 
                              'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são',
                              'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja',  'sejamos',
                              'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão',
                              'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve',
                              'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem',
                              'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam'])
            
            wordcloud = WordCloud(stopwords = stopwords, background_color='black', width= 3200, height=1600).generate(self.data)

        return wordcloud.to_file('tmp/wordcloud.png')
