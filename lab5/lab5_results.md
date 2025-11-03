# Names: Josh Garbi, Josh Bielas
# Lab: Lab5 (Multimodal AI with Ollama)
# Date: 11-3-25

## Compare this to zero-shot. Does adding guidelines help? In what situations do the guidelines seem to matter most?
 - there was some unexpected behavior with zero shot. It would seem convinced with a class even when that class was removed from the choices. I was able to change the selected one from "building" to "tower".

 - When guidlines are added the model would accuratly follow them when classifying an image. The guidlines mattered more when the classification was somewhat ambiguous 

## Does the object count seem accurate?

 - It could accuratly count strings on a violin but we noted that the dice were a problem for the LLM because one was partially hidden by another.