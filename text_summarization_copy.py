import math
from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
ps=PorterStemmer()
import csv
import os
path='C:\\Users\\saite\\Desktop\\SPORTS\\'

files=["bbcsport3.txt"]
'''for r,d,f in os.walk(path):
    for file in f:
        if('.txt' in file):
            files.append(os.path.join(r,file))'''



no_of_files=0
for input_file in files:
    #print(input_file)
    print(input_file)
    no_of_files+=1
    f = open(input_file, "r",encoding="utf8")

    m=[]
    #dividing in to sentences from file
    for line in f:
        l=line.split(".")
        m.append(l)
    print(m)
    sentence=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
            sentence.append(m[i][j])

    #lowercasing
    for i in range(len(sentence)):
        #sentence[i]=sentence[i]+'.'
        sentence[i]=sentence[i].lower()
    print(sentence)

    #stop word removal

    stopwords=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other', 'off', 'is', 's','am','or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than','\n.','.','']
    stopwords_without_pronouns=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other', 'off', 'is', 's','am','or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than','\n.','.','']
    words=[]
    for i in range(len(sentence)):
        words.append(sentence[i].split(" "))
    print(words)
    words_after_stopword_removal=[[] for x in range(len(words))]
    print(words_after_stopword_removal)
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(words[i][j] not in stopwords):
                words_after_stopword_removal[i].append(words[i][j])
    print(words_after_stopword_removal)

    #stemming

    words_after_stemming=[[] for x in range(len(words))]
    for i in range(len(words_after_stopword_removal)):
        for j in range(len(words_after_stopword_removal[i])):
            words_after_stemming[i].append(ps.stem(words_after_stopword_removal[i][j]))
    print(words_after_stemming)

    #TF-ISF
    tfisf=[[] for x in range(len(words))]
    N=len(words_after_stemming)
    for i in range(len(words_after_stemming)):
        for j in range(len(words_after_stemming[i])):
            tf=words_after_stemming[i].count(words_after_stemming[i][j])
            s=words_after_stemming[i][j]
            c=0
            for x in range(len(words_after_stemming)):
                if(s in words_after_stemming[x]):
                    c+=1
            isf=math.log((N/c),10)
            tfisf[i].append(tf*isf)
    print(tfisf)
    tfisf_for_each_sentence=[[] for x in range(len(words))]
    for i in range(len(tfisf)):
        c=0
        for j in range(len(tfisf[i])):
            c+=tfisf[i][j]
        tfisf_for_each_sentence[i].append(c)
    print(tfisf_for_each_sentence)


    #sentence length
    count_of_words_in_sentence=[[] for x in range(len(words))]
    sentence_length=[[] for x in range(len(words))]
    maximum_length=0
    for i in range(len(words_after_stemming)):
        c=len(words_after_stemming[i])
        count_of_words_in_sentence[i].append(c)
        if(maximum_length<c):
            maximum_length=c
    print(count_of_words_in_sentence)
    print(maximum_length)
    for i in range(len(count_of_words_in_sentence)):
        sentence_length[i].append(count_of_words_in_sentence[i][0]/maximum_length)
    print(sentence_length)

    #proper nonu
    if_propernoun_available=[[0] for x in range(len(words))]
    print(if_propernoun_available)
    for i in range(len(words_after_stemming)):
        flag=0
        for j in range(len(words_after_stemming[i])):
            l=pos_tag(words_after_stemming[i][j].split())
            print(l)
            if(l[0][1]=='NN'):
                flag=1
                break
            elif(l==[]):
                continue
        if(flag==1):
            if_propernoun_available[i][0]=1
            flag=0
    print(if_propernoun_available)

    #pronoun
    if_pronoun_available=[[0] for x in range(len(words))]
    print(if_pronoun_available)
    for i in range(len(words_after_stemming)):
        flag=0
        for j in range(len(words_after_stemming[i])):
            l=pos_tag(words_after_stemming[i][j].split())
            if(l[0][1]=='PRP'):
                flag=1
                break
        if(flag==1):
            if_pronoun_available[i][0]=1
            flag=0
    print(if_pronoun_available)


    #sentence position
    pos=[[0] for x in range(len(words))]
    num=len(words)
    print(num)
    for i in range(1,num+1):
        pos[i-1][0]=(i/num)
    print(pos)


    print("words after stemming:",words_after_stemming)
    #sentence containing scores
    score=[[0] for x in range(len(words))]
    flag=0
    flag1=0
    for i in range(len(words_after_stemming)):
        flag=0
        for j in range(len(words_after_stemming[i])):
            flag1=0
            for k in range(len(words_after_stemming[i][j])):
                if(('0' in words_after_stemming[i][j][k]) or ('1' in words_after_stemming[i][j][k])or ('2' in words_after_stemming[i][j][k]) or ('3' in words_after_stemming[i][j][k]) or ('4' in words_after_stemming[i][j][k]) or ('5' in words_after_stemming[i][j][k]) or  ('6' in words_after_stemming[i][j][k]) or  ('7' in words_after_stemming[i][j][k]) or  ('8' in words_after_stemming[i][j][k]) or  ('9' in words_after_stemming[i][j][k])):
                    flag=1
                    flag1=1
                    break
            if(flag1==1):
                flag1=0
                break
        if(flag==1):
            score[i][0]=1
            flag=0
        else:
            score[i][0]=0
    print("score:\n",score)


    #cosine similarity
    all_words=[]
    for i in range(len(words_after_stemming)):
        for j in range(len(words_after_stemming[i])):
            all_words.append(words_after_stemming[i][j])
    print(all_words)
    vector=[[0]*len(all_words) for x in range(len(words))]
    print(vector)

    for i in range(len(words_after_stemming)):
        for j in range(len(all_words)):
            vector[i][j]=words_after_stemming[i].count(all_words[j])
    print(vector)

    cosine_similarity=[[] for x in range(len(words))]
    print(cosine_similarity)
    for i in range(len(vector)):
        vec1=vector[i]
        print(vec1)
        for j in range(len(vector)):
            vec2=vector[j]
            dot=0
            for k in range(len(vec1)):
                dot+=(vec1[k]*vec2[k])
            c1=0
            for k in range(len(vec1)):
                c1+=(vec1[k]**2)
            c1=(c1**0.5)
            c2=0
            for k in range(len(vec2)):
                c2+=(vec2[k]**2)
            c2=(c2**0.5)
            try:
                cosine_similarity[i].append((dot)/(c1*c2))
            except ZeroDivisionError:
                cosine_similarity[i].append(0.0)
    print(cosine_similarity)

    final_cosine=[[0] for x in range(len(words))]
    for i in range(len(cosine_similarity)):
        p=0
        for j in range(len(cosine_similarity[i])):
            p+=cosine_similarity[i][j]
        final_cosine[i][0]=(p/len(cosine_similarity[i]))
    print(final_cosine)

    mean_of_tfisf_and_cs = [[0] for x in range(len(words))]

    for i in range(len(cosine_similarity)):
        mean_of_tfisf_and_cs[i][0]=(cosine_similarity[i][0]+tfisf_for_each_sentence[i][0])/2
    print(mean_of_tfisf_and_cs)

    dict = {}
    for i in range(len(mean_of_tfisf_and_cs)):
        dict[i] = mean_of_tfisf_and_cs[i][0]

    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1],reverse=True)

    print("\n\n\n")
    print("tfisf:\n",tfisf_for_each_sentence)
    print("\n\n\n")
    print("sentence length:\n",sentence_length)
    print("\n\n\n")
    print("proper noun:\n",if_propernoun_available)
    print("\n\n\n")
    print("pronoun:\n",if_pronoun_available)
    print("\n\n\n")
    print("sentence position:\n",pos)
    print("\n\n\n")
    print("scores:\n",score)
    print("\n\n\n")
    print("cosine_similarity:\n",final_cosine)
    print("\n\n\n")
    print(mean_of_tfisf_and_cs)
    print("\n\n\n")
    print(dict)
    print("\n\n\n")
    print(sorted_dict)
    print("\n\n\n")


    #print("enter w1:")
    w1=0.8#float(input())
    #print("enter w2:")
    w2=0.6#float(input())
    #print("enter w3:")
    w3 =0.4#float(input())
    #print("enter w4:")
    w4 =0.2 #float(input())
    #print("enter w5:")
    w5 =0.3 #float(input())
    #print("enter w6:")
    w6 =0.5 #float(input())
    #print("enter w7:")
    w7 =0.7 #float(input())

    input_multiplied_by_weight = [[0] for x in range(len(words))]

    for i in range(len(words)):
        input_multiplied_by_weight[i][0]=(w1*tfisf_for_each_sentence[i][0])+(w2*sentence_length[i][0])+(w3*if_propernoun_available[i][0])+(w4*if_pronoun_available[i][0])+(w5*pos[i][0])+(w6*score[i][0])+(w7*final_cosine[i][0])

    print(input_multiplied_by_weight)

    sigmoid_activation_func = [[0] for x in range(len(words))]
    for i in range(len(words)):
        sigmoid_activation_func[i][0]=1/(1+math.exp(input_multiplied_by_weight[i][0]*-1))

    print(sigmoid_activation_func)

    dict1 = {}
    for i in range(len(mean_of_tfisf_and_cs)):
        dict1[i] = sigmoid_activation_func[i][0]

    print(dict1)

    sorted_dict1 = sorted(dict1.items(), key=lambda kv: kv[1], reverse=True)

    print(sorted_dict1)

    compression_ratio=int(len(mean_of_tfisf_and_cs)*0.5)
    print(compression_ratio)
    output_lines=[]
    for i in range(compression_ratio):
        output_lines.append(sorted_dict[i][0])
    print(output_lines)

    output_lines.sort()
    print(output_lines)

    output=""
    for i in output_lines:
        output=output+m[0][i]+". "
    print(output)
    print("\n\n\n")



    output_lines1 = []
    for i in range(compression_ratio):
        output_lines1.append(sorted_dict1[i][0])
    print(output_lines1)

    output_lines1.sort()
    print(output_lines1)

    output1 = ""
    for i in output_lines1:
        output1 = output1 + m[0][i] + ". "
    print(output1)

    print(output_lines)
    print(output_lines1)

    total_lines=output_lines+output_lines1
    lines_after_set=list(set(total_lines))
    print(lines_after_set)

    output_afer_set = ""
    for i in lines_after_set:
        output_afer_set = output_afer_set + m[0][i] + ". "
    print(output_afer_set)



    with open('csv_data_test'+str(no_of_files)+".csv",'w',newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(["TFISF","Sentence Length","Proper noun","Pronoun","Sentence position","Scores","Cosine similarity"])
        for i in range(len(tfisf)):
            writer.writerow([tfisf_for_each_sentence[i][0],sentence_length[i][0],if_propernoun_available[i][0],if_pronoun_available[i][0],pos[i][0],score[i][0],final_cosine[i][0]])


