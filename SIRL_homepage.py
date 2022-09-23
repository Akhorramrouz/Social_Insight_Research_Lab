from dis import disco
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageOps


  
def show_circular_image(path, size=(200, 200)):
    """Show a circular image"""
    img=Image.open(path)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output



st.title("Social Insight Research Lab")


with st.sidebar:
    st.image('logo.png',use_column_width=1)

    st.write("Navigate to the page you want to visit")
    pages = ["Home", "People", "Publications", "Contact"]
    page = st.radio("Go to", pages)
    
if page == "Home":
    st.write("# Homepage")
    st.write("###### Welcome to the homepage of the Social Insight Research Lab at Rochester Institute of Technology.")
    
    st.write("#### About")
    st.write("""
    
    The researches Social Insight Research Lab focus is in Computational Social Science. In this field, we are interested in
    analyzing globally important events in Asia and developing methods for noisy social media texts generated in this linguistically diverse region.
     
    Our projects geared towards humanitarian good. We are focusing on analyzing how internet users from different linguistic backgrounds 
    (e.g., geographic regions with a large number of English-as-first-language speakers, geographic regions with a 
    large number of English-as-second-language speakers, or geographic regions with a large number of multilingual 
    speakers) and abilities have shared health compliance information during the ongoing COVID-19 pandemic and 
    develop new natural language processing methods to facilitate effective identification of health compliance 
    information in languages with fewer computational linguistic resources (e.g., Hindi and Farsi). 
    
    Our other broad focus is US politics""")
elif page == "People":
    st.write("# People")

    images, discriptions = st.columns([2,5],)
    with images:
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.image(show_circular_image('Ashique.jpg'), caption= "Ashique KhudaBukhsh",
        width=200)

    with discriptions:
        st.subheader("Assistant Professor")
        st.write("Ashique KhudaBukhsh is currently an Assistant Professor at RIT. Prior to this role, he was a Project Scientist at CMU mentored by Prof. Tom Mitchell. He was a postdoc mentored by Prof. Jaime Carbonell. His current research focus is in Computational Social Science. In this field, he is interested in analyzing globally important events in South East Asia and developing methods for noisy social media texts generated in this linguistically diverse region. His other broad focus is US politics; he has offered a graduate course (team-taught with Prof. Mark S. Kamlet and Prof. Tom M. Mitchell) at the intersection of machine learning and political science focusing on the 2020 US election. A detailed resume can be found here. He is also a head of the RIT Social Insight Research Lab (SIRL).")


    st.write("---")
    images, discriptions = st.columns([2,5])
    with images:
        st.image(show_circular_image('Sujan.jpg'), caption= "Sujan Dutta",
        width=185)

    with discriptions:
        st.subheader("PhD Candidate")

    st.write("---")
    images, discriptions = st.columns([1,3])
    with images:
        st.image(show_circular_image('Adel.jpg'), caption= "Adel Khorramrouz",
        width=175)

    with discriptions:
        st.subheader("M.Sc Candidate")

    st.write("---")
    images, discriptions = st.columns([1,3],)
    with images:
        st.image(show_circular_image('Seyd.jpg'), caption= "Syed Mohammad Sualeh A.",
        width=175)

    
    with discriptions:
        st.subheader("M.Sc Candidate")

    



elif page == "Publications":

    st.write("# Publications")

    st.markdown("""
    <ul>    <li><strong><em>A Murder and Protests, the Capitol Riot, and the Chauvin Trial: Estimating
Disparate News Media Stance.</strong></em> Sujan Dutta, Beibei Li, Daniel S. Nagin, Ashiqur R. KhudaBukhsh. International Joint Conference on Artificial Intelligence, (IJCAI-ECAI 2022).<strong> <font color="red">Oral presentation, 15%</font></strong>.</li> 
	<li><strong><em>Conversational Inequality Through the Lens of Political Interruption.</strong></em> Clay H. Yoo, Jiachen Wang, Yuxi Luo, Kunal Khadilkar, Ashiqur R. KhudaBukhsh. International Joint Conference on Artificial Intelligence, (IJCAI-ECAI 2022).<strong> <font color="red">Oral presentation, 15%</font></strong>.</li>
	<li><strong><em>Fringe News Networks: Dynamics of US News Viewership following the 2020 Presidential Election.</em></strong> Ashiqur R. KhudaBukhsh*, Rupak Sarkar*, Mark S. Kamlet, Tom M. Mitchell. The 14th International ACM Conference on Web Science in 2022 (WebSci'22). [<a href="https://arxiv.org/pdf/2101.10112.pdf">Preprint</a>].</li> 
	<li><strong><em> Gender Bias, Social Bias, and Representation in Bollywood and Hollywood</em></strong>. Kunal Khadilkar*, Ashiqur R. KhudaBukhsh*, Tom M. Mitchell. Cell Press Patterns.[<a href="https://www.cell.com/patterns/pdf/S2666-3899(21)00283-X.pdf">Paper</a>].</li> 
	<li><strong><em>'Beach' to 'Bitch': Inadvertent Unsafe Transcription of Kids' Content on YouTube</em></strong>. Krithika Ramesh, Ashiqur R. KhudaBukhsh, Sumeet Kumar. 36th AAAI Conference on Artificial Intelligence (AAAI), 2022.[<a href="https://arxiv.org/pdf/2203.04837.pdf">Preprint</a>]</li> 
    <li><strong><em>Empathy and Hope: Resource Transfer to Model Inter-Country Social Media Dynamics</em></strong>. Clay H. Yoo, Shriphani Palakodety, Rupak Sarkar, Ashiqur R. KhudaBukhsh. 1st Workshop on NLP for Positive Impact <strong>(NLP4PI)</strong>, ACL 2021. [<a href="https://arxiv.org/pdf/2106.12044.pdf">Paper</a>][<a href="https://github.com/anton-sturluson/empathy-and-hope">Data</a>] </li>    
	<li><strong><em>Exploring Polarization of Users Behavior on Twitter During the 2019 South American Protests</em></strong>. Ramon Villa-Cox, Helen Zeng, Ashiqur R. KhudaBukhsh, Kathleen M. Carley - 7th International Conference on Computational Social Science (IC2S2), 2021. <strong><font color="gray"> Abstract.</strong> </font></li>  
	<li><strong><em>We Don't Speak the Same Language: Interpreting Polarization Through Machine Translation</em></strong>. A. R. KhudaBukhsh*, Rupak Sarkar*, Mark S. Kamlet, Tom M. Mitchell - 35th AAAI Conference on Artificial Intelligence (AAAI), 2021.<strong><font color="red">Oral presentation, 21%.</font></strong>[<a href="https://arxiv.org/pdf/2010.02339.pdf">Preprint</a>][<a href="https://github.com/styx97/PolarizationAAAI2021">Code</a>].</li>
	<li><strong><em>Social Media Attributions in the Context of Water Crisis</em></strong>. Rupak Sarkar*, Sayantan Mahinder*, Hirak Sarkar, A. R. KhudaBukhsh - IJCAI 2020 AI for Social Good Workshop.</li>
	<li><strong><em>An Unfair Affinity Toward Fairness: Characterizing 70 Years of Social Biases in B<sup>H</sup>ollywood.</strong></em> Kunal Khadilkar, A. R. KhudaBukhsh - IJCAI 2020 AI for Social Good Workshop.<strong><font color ="red"> Long talk.</font></strong></li>
	<li><strong><em>Are Chess Discussions Racist? An Adversarial Hate Speech Data Set (Student Abstract).</strong></em> Rupak Sarkar, A. R. KhudaBukhsh - 35th AAAI Conference on Artificial Intelligence (AAAI), 2021.<strong><font color="red"> Best AAAI-21 Student Abstract 3-Minute Presentation.</font></strong> [<a href="https://arxiv.org/pdf/2011.10280.pdf">Preprint]</a>[<a href="AAAI-2021-Chess-Poster.pdf">Poster</a>][<a href="https://studio.slideslive.com/web_recorder/share/20210108T225112Z__AAAI__sa-379__are-chess-discussions-racist?s=a1526f03-dbf2-4a0f-888e-f693f3a59633">Presentation</a>][<a href="https://github.com/styx97/chess_racism">Data</a>].</li>
	<li><strong><em>An Unfair Affinity Toward Fairness: Characterizing 70 Years of Social Biases in B<sup>H</sup>ollywood (Student Abstract).</strong></em> Kunal Khadilkar, A. R. KhudaBukhsh - 35th AAAI Conference on Artificial Intelligence (AAAI), 2021.</li>
	<li><strong><em>Social Media Attributions in the Context of Water Crisis</em></strong>. Rupak Sarkar*, Sayantan Mahinder*, Hirak Sarkar, A. R. KhudaBukhsh - Empirical Methods in Natural Language Processing (EMNLP), 2020.</li><strong><font color=red>Long paper, 22.4%.</font></strong> [<a href="https://github.com/styx97/water_crisis">Data</a>]</li>
	<li><strong><em>An Unfair Affinity Toward Fairness: Characterizing 70 Years of Social Biases in B<sup>H</sup>ollywood.</strong></em> Kunal Khadilkar, A. R. KhudaBukhsh. 4th Workshop on <strong>(NLP+CSS)</strong>, EMNLP 2020.</li>	
	<li><strong><em>Annotation Efficient Language Identification from Weak Labels</em></strong>. Shriphani Palakodety*, A. R. KhudaBukhsh* - 6th Workshop on Noisy User-generated Text <strong>(W-NUT)</strong>, EMNLP 2020.</li> 
	<li><strong><em>The Non-native Speaker Aspect: Indian English in Social Media</em></strong>. Rupak Sarkar, Sayantan Mahinder, A. R. KhudaBukhsh - 6th Workshop on Noisy User-generated Text <strong>(W-NUT)</strong>, EMNLP 2020.</li> 	
	<li><strong><em>On NLP Methods Robust to Noisy Indian Social Media Data</em></strong>. A. R. KhudaBukhsh*, Shriphani Palakodety*, Jaime G. Carbonell - AI for Social Good, Harvard CRCS Workshop. 2020.<font color ="red"><strong> Contributed talk. </font></strong>[<a href ="Harvard-CRCS-AI4SG.pdf"> CRC</a>]</li>
	<li><strong><em>Harnessing Code Switching to Transcend the Linguistic Barrier</em></strong>. A. R. KhudaBukhsh*, Shriphani Palakodety*, Jaime G. Carbonell - International Joint Conference on Artificial Intelligence-Pacific Rim International Conference on Artificial Intelligence, Special Track on Computational Sustainability and Human Well-being (IJCAI-PRICAI).  2020.<font color = "red"> <strong> Oral presentation, 12.7%.</font></strong> [<a href = "https://arxiv.org/pdf/2001.11258.pdf">Preprint</a>][<a href = "https://www.ijcai.org/Proceedings/2020/0602.pdf">CRC</a>]</li>
	<li><strong><em>Hope Speech Detection: A Computational Analysis of the Voice of Peace</em></strong>. Shriphani Palakodety*, A. R. KhudaBukhsh*, Jaime G. Carbonell - Twenty-Fourth European Conference on Artificial Intelligence (ECAI), 2020.<font color = "red"> <strong> Oral presentation, 26.8%.</font></strong> [<a href = "https://arxiv.org/pdf/1909.12940.pdf">Preprint</a>][<a href = "ECAI-2019-HopeSpeech.pdf">CRC</a>][<a href = "http://blog.shriphani.com/2020/02/03/polyglot-word-embeddings-discover-language-clusters/">Blog</a>]</li>
	<li><strong><em>Mining Insights from Large-scale Corpora Using Fine-tuned Language Models</em></strong>. Shriphani Palakodety*, A. R. KhudaBukhsh*, Jaime G. Carbonell - Twenty-Fourth European Conference on Artificial Intelligence (ECAI), 2020. <font color = "red"> <strong> Oral presentation, 26.8%.</font></strong> [<a href = "">Preprint</a>][<a href ="ECAI-2019-BERTElection.pdf">CRC</a>]</li>
<li><strong><em>The Refugee Experience Online: Surfacing Positivity Amidst Hate</em></strong>. Shriphani Palakodety*, A. R. KhudaBukhsh*, Jaime G. Carbonell - Twenty-Fourth European Conference on Artificial Intelligence (ECAI), 2020. [<a href = "">Preprint</a>]</li>	
<li><strong><em>Voice for the Voiceless: Active Sampling to Detect Comments Supporting the Rohingyas</em></strong>. Shriphani Palakodety*, A. R. KhudaBukhsh*, Jaime G. Carbonell - Thirty-Fourth AAAI Conference on Artificial Intelligence, AI for Social Impact Track (AAAI), 2020. <font color = "red"> <strong> Oral presentation, 5.74%. </strong></font>[<a href = "https://arxiv.org/pdf/1910.03206.pdf">Preprint</a>][<a href ="https://aaai.org/Papers/AAAI/2020GB/AISI-PalakodetyS.130.pdf">PDF CRC</a>]</li>
<li><strong><em>Toward Reciprocity-aware Distributed Learning in Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell - Sixteenth Pacific Rim Conference on Artificial Intelligence (PRICAI), 2019. [<a href = "">PDF CRC</a>]</li>
<li><strong><em>Expertise Drift in Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell - Journal of Autonomous Agents and Multi-Agent Systems (JAAMAS), 2019. [<a href = "https://rdcu.be/bNldG">PDF CRC</a>]</li>
<li><strong><em>Endorsement in Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell - Sixteenth European Conference on Multi-Agent  Systems (EUMAS-18), 2018.
     [<a
    href="">PDF CRC</a>]</li>
<li><strong><em>Market-aware Proactive Skill Posting</em></strong>. A. R. KhudaBukhsh, Jong Woo Hong,  Jaime G. Carbonell - Twenty-Fourth International Symposium on Methodologies for Intelligent Systems (ISMIS-18), 2018.
     [<a
    href="ISMIS2018.pdf">PDF CRC</a>]</li>
<li><strong><em>Robust learning in referral networks: a comparative analysis</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell, Peter J. Jansen - Journal of Intelligent Information Systems (JIIS), June, 2018.
     [<a
    href="https://rdcu.be/14FW">PDF CRC</a>]</li>
<li><strong><em>Expertise Drift in Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell - International Conference on Autonomous Agents and Multiagent Systems (AAMAS-18), 2018. <font color = "red"> <strong>Oral presentation 6.7%.</strong></font>
     [<a
    href="AAMAS2018.pdf">PDF CRC</a>]</li>
<li><em><strong>Distributed Learning in Referral Networks </strong></em>. A. R. KhudaBukhsh
 - PhD thesis, 2017. [<a
    href="KhudaBukhsh-Thesis.pdf">PDF</a>]</li>



<li><strong><em>Incentive Compatible Proactive Skill Posting in Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell, Peter J. Jansen - Fifteenth European Conference on Multi-Agent Systems (EUMAS-17), 2017.
    [<a
href="EUMAS2017.pdf">PDF CRC</a>]</li>

<li><strong><em>Robust Learning in Expert Networks: A Comparative Analysis</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell, Peter J. Jansen - Twenty-Third International Symposium on Methodologies for Intelligent Systems (ISMIS-17), 2016.
    [<a
href="ISMIS2017.pdf">PDF CRC</a>]</li>

<li><strong><em>Proactive-DIEL in Evolving Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell, Peter J. Jansen - Fourteenth European Conference on Multi-Agent Systems (EUMAS-16), 2016.
    [<a
href="EUMAS2016.pdf">PDF CRC</a>]</li>

<li><strong><em>Proactive Skill Posting in Referral Networks</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell, Peter J. Jansen - Twenty-Ninth Australasian Joint Conference on Artificial Intelligence (AI-16), 2016.
     [<a
    href="AI2016.pdf">PDF CRC</a>]</li>

 <li><strong><em>Distributed Learning in Expert Referral Networks</em></strong>. A. R. KhudaBukhsh, Peter J. Jansen, Jaime G. Carbonell - Twenty-Second European
Conference on
Artificial
Intelligence (ECAI-16), 2016.
     [<a    href="ECAI2016.pdf">PDF CRC</a>]</li>

  <li><strong><em>Quantifying the Similarity of Algorithm Configurations</em></strong>. L. Xu*, A. R. KhudaBukhsh*, H. H. Hoos, K.
    Leyton-Brown - Learning and Intelligent Optimization Conference (LION10), 2016.
     [<a
    
href="http://www.cs.ubc.ca/~kevinlb/pub.php?u=2016-LION-Visualizing-Configurations.pdf">PDF CRC</a>]</li>


 <li><strong><em>Building Effective Query Classifiers: A Case Study in Self-harm Intent Detection</em></strong>. A. R. KhudaBukhsh, Paul N. Bennett, Ryen  W. White - Twenty-Fourth International
Conference on
Information and 
Knowledge Management (CIKM-15), 2015.
     [<a    href="CIKM2015.pdf">PDF CRC</a>]</li>


  <li><strong><em>SATenstein: Automatically Building Local Search SAT Solvers
    From Components</em></strong>. A. R. KhudaBukhsh*, L. Xu*, H. H. Hoos, K.
    Leyton-Brown - Artificial Intelligence Journal (AIJ), volume 232, pp. 20-42, March 2016.
     [<a
    
href="http://www.cs.ubc.ca/labs/beta/Projects/SATenstein/2016-AIJ-SATenstein.pdf">Preprint</a>]</li>

  <li><strong><em>SATenstein: Automatically Building Local Search SAT Solvers
    From Components</em></strong>. A. R. KhudaBukhsh, L. Xu, H. H. Hoos, K.
    Leyton-Brown - Twenty-First International Joint Conference on Artificial
    Intelligence (IJCAI-09), 2009. [<a
    
href="http://www.cs.ubc.ca/labs/beta/Projects/SATenstein/SATenstein_ijcai.pdf">PDF 
CRC</a>]</li>

 <li><strong><em>Detecting Non-adversarial Collusion in Crowdsourcing</em></strong>. A. R. KhudaBukhsh, Jaime G. Carbonell, Peter  J. Jansen - Twenty-Fourth International
Conference on Human Computation and Crowdsourcing (HCOMP), 2014.
     [<a    href="HCOMP-2014.pdf">PDF CRC</a>]</li>


  <li><em><strong>SATenstein: Automatically Building Local Search SAT Solvers From Components </strong></em>. A. R. KhudaBukhsh
 - master thesis, 2009. [<a
    href="http://www.cs.ubc.ca/labs/beta/Projects/SATenstein/ashique_masters_thesis.pdf">PDF</a>]</li>
</ul>""",unsafe_allow_html=True)
elif page == "Contact":
    st.write("# Contact")
