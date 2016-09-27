from __future__ import division
import re
 
class TextReduce(object):
 
    def toSent(self, content):
        content = content.replace("\n", ". ");
        return content.split(". ");
 
    def toPara(self, content):
        return content.split("\n\n");
 
    def sentIntersection(self, sent1, sent2):
        s1 = set(sent1.split(" "));
        s2 = set(sent2.split(" "));
 
        if (len(s1) + len(s2)) == 0:
            return 0;
 
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2);
 
    def formatSent(self, sentence):
        sentence = re.sub(r'\W+', '', sentence);
        return sentence;
 
    # Convert the content into a dictionary <K, V>; k = The formatted sentence, V = The rank of the sentence
    def getSentRanks(self, content):
 
        sentences = self.toSent(content);
 
        # Calculate the intersection of every two sentences
        n = len(sentences);
        values = [[0 for x in xrange(n)] for x in xrange(n)];
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentIntersection(sentences[i], sentences[j]);
 
        # Sentences dictionary, the score of a sentences is the sum of all its intersection
        sentences_dic = {};
        for i in range(0, n):
            score = 0;
            for j in range(0, n):
                if i == j:
                    continue;
                score += values[i][j];
            sentences_dic[self.formatSent(sentences[i])] = score;
        return sentences_dic;
 
    def get_best_sentence(self, paragraph, sentences_dic):
 
        sentences = self.toSent(paragraph);
 
        # Ignore short paragraphs
        if len(sentences) < 2:
            return "";
 
        # Get the best sentence according to the sentences dictionary
        best_sentence = "";
        max_value = 0;
        for s in sentences:
            strip_s = self.formatSent(s);
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s];
                    best_sentence = s;
 
        return best_sentence;
 
    def get_summary(self, content, sentences_dic):
 
        paragraphs = self.toPara(content);
 
        summary = [];
        summary.append("");
 
        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip();
            if sentence:
                summary.append(sentence);
 
        return ("\n").join(summary);
 
def main():
 
    content = """
Early South Africa

Over a hundred thousand years ago people in what is now South Africa lived by hunting animals and gathering plants. They used stone tools. Then about 2,000 years ago people in the west learned to herd sheep and cattle. About 200 AD people mixed farming (growing crops as well as raising livestock) and iron tools were introduced into the east of South Africa.

At the end of the 15th Century the Portuguese sailed past the Cape of Good Hope. However it was not until 1652 that the Europeans founded a colony in South Africa. In 1652 the Dutch, led by Jan van Riebeeck founded a base where ships travelling to the Far East could be supplied. From 1658 the Dutch imported slaves into South Africa. Meanwhile, at first the Europeans traded with the native people but they soon fell out. In 1658 they fought their first war, the first of many.

Gradually the Dutch colony in South Africa expanded and from 1688 French Huguenots (Protestants) arrived fleeing religious persecution. Slowly the native people were driven from their land and in 1713 many died in a smallpox epidemic.


British South Africa

In 1795 the British captured Cape Colony (South Africa). They handed it back to the Dutch in 1803 but took it again in 1806. In 1814 a treaty confirmed British ownership of Cape Colony. In 1812 the British founded Grahamstown and in 1820 4,000 Britons were granted land by the Great Fish River.

The Boers (Dutch settlers) in South Africa resented British rule. When slavery was abolished in 18344 they were antagonized still more. Finally the Boers began a mass migration away from the British called the Great Trek. In 1838 the Boers fought and defeated the Zulus at the battle of Blood River. Eventually the Boers founded two republics away from the British, Orange Free State and Transvaal. In the 1850s the British recognized the two Boer republics.

However the situation changed in 1867 when diamonds were found in Northern Cape. In 1871 diamonds were also found at Kimberley. Gold was discovered at Gaueng in 1886.

Meanwhile in 1879 the British fought the Zulus in South Africa. The British were badly defeated by the Zulus at the Isandhlwana but they went on to win the war.

Increasingly the British were keen to bring all of South Africa, including the Boer republics under their control. In 1884 Lesotho became a British protectorate. In 1894 the Kingdom of Swaziland became a protectorate.

Meanwhile British settlers had moved into the Transvaal Republic. The Boers called them Uitlanders (foreigners). Cecil Rhodes was Prime Minister of British South Africa from 1890 to 1895 and in 1895 he plotted a rebellion by Uitlanders in the Transvaal, which would be supported by a force from South Africa led by Leander Starr Jameson. The aim was to overthrow the government of Paul Kruger, President of the Transvaal. However the Jameson Raid of January 1896 was defeated by the Boers and Jameson himself was captured. The two Boer republics formed and alliance and hostility between them and the British grew.

Finally in October 1899 war began in South Africa between the Boers and the British. At first the Boers were successful but in 1900 more British troops arrived and the Boers were pushed back. The Boers then turned to guerrilla warfare. However Kitchener, the British commander began herding Boer women and children into concentration camps where more than 20,000 of them died of disease.


20th Century South Africa

The Boers finally surrendered in 1902 and the British annexed the Boer republics. In 1910 a United South Africa was given a constitution. It became known as the Union of South Africa.

From the start black people were very much second-class citizens in South Africa. Most lived in tribal reserves and laws of 1913 and 1936 prevented them owning land outside certain areas. Most blacks were not allowed to vote. In 1912 black South Africans founded the South African National Congress (later the ANC) but at first they achieved little.

In 1914 South Africa joined the First World War against Germany. That year there was a rebellion by the Boers, which was crushed. In 1918 Afrikaners (descendants of Dutch settlers) founded a secret organisation called the Broederbond (brotherhood).

In 1939 South Africa joined the Second World War against Germany. However some Afrikaners opposed this decision.

In 1948 the National Party came to power in South Africa. The party introduced a strict policy of apartheid (separateness). Whites and blacks were already segregated to a large degree. New laws made segregation much stricter.

However in 1955 organisations representing black people, white people, coloureds and Indians formed the Congress Alliance. In 1955 they adopted the Freedom Charter. Yet divisions soon occurred. In 1958 some black South Africans broke away from the ANC and they formed the pan Africanist Congress or PAC. They were led by Robert Sobukwe.

In 1960 both the ANC and the PAC planned demonstrations against the pass laws, which restricted the movements of black people. On 21 March 1960 Sobukwe led thousands of people in a demonstration. In Sharpeville the police fired at them killing 69. The government banned the ANC and the PAC. And in 1963 Nelson Mandela was sentenced to life imprisonment.

Meanwhile in 1961 South Africa left the Commonwealth and became a republic.

In 1966 Prime Minister Mendrik Verwoerd was assassinated but otherwise South Africa was quiet until 1976, although naturally black resentment continued to simmer below the surface.

Rioting began in Soweto on 16 June 1976. The riots spread and they continued into 1977. In 1978 P W Botha became prime minister. He was determined to continue apartheid and in 1983 he introduced a new constitution with a tri-cameral parliament, with houses for whites, coloreds and Indians (with no representation for blacks). However the new constitution pleased nobody. Meanwhile other countries were increasingly imposing economic sanctions on South Africa and inside the country resistance to apartheid grew. In 1989 Botha was forced from office. He was replaced by Willem de Klerk who in 1990 pledged to end apartheid. He also released Nelson Mandela. De Klerk introduced a new constitution with rights for all. The first democratic elections were held in April 1994 and in May 1994 Nelson Mandela was elected president. He retired in 1999.


21st Century South Africa

In the early 21st century the economy of South Africa grew but recently it has slowed. South Africa suffers from high unemployment. The country also suffers from widespread poverty. However tourism in South Africa is an important industry. South Africa is also rich in minerals. Today the population of South Africa is 53 million.
    """;
     
    reducer = TextReduce();
    sentences_dic = reducer.getSentRanks(content);
    summary = reducer.get_summary(content, sentences_dic);
 
    print summary;
    print "";
    print "Original Length 	:  %s" % len(content);
    print "Summary Length	 	:  %s" % len(summary);
    print "Summary Ratio		:  %s" % (100 * (len(summary) / len(content)));
 
if __name__ == '__main__':
    main();