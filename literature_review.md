# Literature review

I started with a small set of papers rather than trying to collect everything written about ECG machine learning. I wanted the reading to answer a few practical questions before I touched the data.

I wanted to know what PTB-XL actually contains and how it is normally evaluated, why amplitude is relevant to the HYP task, what recent work has found about preprocessing, and where my question still has room to be tested.

## How I chose the papers

Most of the papers below are peer-reviewed research articles. I also used the main PTB-XL dataset paper and an international clinical consensus statement because they answer questions that a machine learning paper alone cannot.

I included one preprint because it deals directly with ECG preprocessing and raises the same methodological concern from other datasets. I am keeping it separate from the peer-reviewed evidence.

I kept the first pass small and stopped when the papers were no longer changing the way I was thinking about the experiment.

## PTB-XL dataset

Wagner et al. 2020  
Scientific Data  
DOI 10.1038/s41597-020-0495-6

This is the main source I am using for the dataset itself. The published paper describes the PTB-XL records, annotations and the recommended way of splitting the data for machine learning.

I am also recording version 1.0.3 separately because that is the version I will actually use.

## PTB-XL benchmarking

Strodthoff et al. 2021  
IEEE Journal of Biomedical and Health Informatics  
DOI 10.1109/JBHI.2020.3022989

I used this paper to understand how PTB-XL has been used as a benchmark rather than simply as a large ECG collection. It is also useful for thinking about evaluation and comparability between models.

It reinforced my decision to use the dataset's own patient-aware folds rather than making up a random split.

## ECG preprocessing review

Safdar et al. 2024  
Computers in Biology and Medicine  
DOI 10.1016/j.compbiomed.2023.107908

I used this as a broad map of ECG preprocessing and machine learning methods. It helped me see how varied preprocessing practice is and where normalization sits in the larger pipeline.

I am not using this review to support a specific claim about whether normalization helps or hurts.

## Clinical reason to care about amplitude

Bacharova et al. 2023  
Journal of Electrocardiology  
DOI 10.1016/j.jelectrocard.2023.08.005

This consensus statement is useful for one very specific reason. Traditional ECG diagnosis of left ventricular hypertrophy relies heavily on QRS voltage criteria, while the clinical literature also points out that voltage is influenced by many factors and that voltage criteria are not especially sensitive on their own.

That gives me a real clinical reason to ask what happens when amplitude is changed before a model sees the signal. It does not mean that amplitude alone defines hypertrophy.

## Recent PTB-XL preprocessing work

Bickmann et al. 2026  
Studies in Health Technology and Informatics  
DOI 10.3233/SHTI260227

This is the paper that most changed my framing.

The authors compared several preprocessing choices across six deep learning architectures on PTB-XL. They tested 24 preprocessing and model combinations and repeated the experiments ten times. The results showed that preprocessing effects depended on the architecture. Some convolutional models did better with raw, unnormalized ECGs while other models behaved differently.

That means my original question was too broad. It is already known that preprocessing can interact with the model. I therefore narrowed my question to whether the same preprocessing choice can also have different consequences across diagnostic tasks when the model and evaluation setup are held constant.

## Recent PTB-XL work on MI and ST/T phenotypes

Jin et al. 2026  
Scientific Reports  
DOI 10.1038/s41598-026-68967-9

I included this paper because it is very recent and uses patient-disjoint evaluation on PTB-XL for MI and ST/T-change phenotypes.

One detail I want to carry into my own work is the authors' treatment of the PTB-XL labels. They describe the primary outcome as an operational ECG phenotype based on the dataset labels rather than as adjudicated active ischemia.

That is a useful reminder for my own interpretation. If I find a difference in an MI task, I will be describing a model's behavior on the PTB-XL label, not claiming that I have built a clinical MI diagnostic test.

## Recent PTB-XL+ work on LVH

Zhou, Luo and Du 2026  
Frontiers in Cardiovascular Medicine  
DOI 10.3389/fcvm.2026.1825829

The authors used PTB-XL+ and included R-wave, S-wave, QRS amplitude and voltage-time features among the predictors used for LVH detection.

I am using it only to support the clinical and computational rationale for keeping HYP as a candidate task. It does not answer my normalization question.

## Supplemental preprocessing evidence

Salimi et al. 2023  
Preprint  
DOI 10.48550/arXiv.2311.04229

This paper directly compares several ECG preprocessing choices, including normalization, across multiple datasets and classifiers. The authors report that min-max normalization was slightly detrimental overall and argue against applying preprocessing blindly.

I am keeping this as supplemental evidence because it is a preprint rather than a peer-reviewed paper. It is still useful because it shows that the concern behind my question is not limited to PTB-XL.

## Additional preprocessing review

Jia et al. 2024  
Bioengineering  
DOI 10.3390/bioengineering11111109

I used this review to get a second view of the broader ECG preprocessing literature, particularly denoising and signal quality issues.

It is background for the methods section rather than evidence for a particular normalization effect.

## Where this leaves the study

After this first pass, I am not comfortable treating ECG preprocessing as universally helpful or neutral.

The reading gave me a more specific question.

Recent work has shown that preprocessing can interact with model architecture. Clinical literature gives me a reason to think carefully about amplitude for hypertrophy. What I now want to test is whether the same preprocessing choice behaves differently across diagnostic tasks when I hold the model and evaluation setup constant.

That is the question I am taking into the data audit.
