# vocal tract tube model   
   
a very simple vocal tract model, few tube model. generate vowel sound by it.  
A python, draw frequency response and cross-sectional view (area) of a very simple vocal tract model, two tube model and three tube model.  
  
[github repository](https://github.com/shun60s/Vocal-Tube-Model)  

There is new version upto five tube model, Vocal-Tube-Model2, in github repository.  

## content    

draw two tube model frequency response and cross-sectional view (area), that corresponds to vocal tract  
```
python main1.py
```
![figure1](docs/freq_resp_vocal_two_tube_model.png)  

  

draw two tube model frequency response and generated waveform, considering glottal voice source and mouth radiation  
save generated waveform as a wav file  
```
python main2.py
```
![figure2](docs/freq_resp_vocal_two_tube_model_with_source_mouth_effect.png)  

  

draw three tube model frequency response and generated waveform, considering glottal voice source and mouth radiation, and cross-sectional view (area)  
save generated waveform as a wav file  
```
python main3.py
```
![figure3](docs/freq_resp_vocal_three_tube_model_with_source_mouth_effect.png)  

  

draw waveform of glottal voice source  
```
python glottal.py
```
![figure4](docs/glottal_waveform.png)  

  

draw frequency response of HPF for simulate mouth radiation  
```
python HPF.py
```
![figure5](docs/freq_resp_HPF.png)  

## Generated sample  

There are sample wav files of generated waveform in the generated_waveform folder  

## Document  

See [Explain-E.pdf](docs/Explain-E.pdf) / [Explain-J.pdf](docs/Explain-J.pdf) in the docs folder  
  
  
## Related link      

- [Speech Waveform Generation by SCILAB](https://wsignal.sakura.ne.jp/onsei2007/scilab456e.html)  
- [Vocal Tube Estimation](https://github.com/shun60s/Vocal-Tube-Estimation/)  

## License    
MIT  
