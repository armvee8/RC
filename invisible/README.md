# Invisible Unicode CLI Tool

A lightweight CLI tool for taking ASCII text and encoding it to Zero Width Joiners and Zero Width Non-Joiners, generate a certain amount of invisible unicode bytes, or convert printable ASCII into invisible Unicode Tag characters that can be converted from invisible unicode. 

## Impetus and Thoughts Behind this Project 
The purpose of this project is to create a lightweight method to experiment with how certain applications, such as sandboxes or databases, might process input that contains invisible unicode. Manual testing and fuzzing can both benefit from this. This tool could be a great way to test for unexpected edge-cases, such as looking at unexpected edge cases within [parser differentials.](https://dev.to/aditya_d_sharma/what-is-a-parser-differential-how-can-the-same-input-mean-different-things-to-different-systems-p4g)

## Installation method:
```
git clone 
cd invisible
python3 -m piip install -e . 
```

## To run the program:
```
invisible_text encode "a cool string"
invisible_text encode-ascii-tags "even cooler string"
invisible_text generate 100 
```