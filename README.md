# word2vecContext
A sample use Word2Vec algorithm to learn tree context

## Some results
------

### Return most similar node:
```python
>>> model.most_similar('A00001/B00001/C00001/D00001')
[('A00001/B00001/C00001/D00002', 0.9907678365707397), ('A00001/B00001/C00001/D00003', 0.9883657097816467), ('A00001/B00001/C00001/D00004', 0.9816274046897888), 
('A00001/B00001/C00001/D00005', 0.9750612378120422), ('A00001/B00001/C00001/D00010', 0.9711226224899292), ('A00001/B00001/C00001/D00008', 0.969694972038269), 
('A00001/B00001/C00001/D00009', 0.9688605070114136), ('A00001/B00001/C00001/D00006', 0.9665477275848389), ('A00001/B00001/C00001/D00007', 0.9633323550224304), 
('A00001/B00001/C00001', 0.7969611287117004)]
```
### Return similarity between nodes
```python
>>> model.similarity(‘A00001/B00001/C00001/D00001’, ‘A00001/B00001/C00001’)
0.79696112054196411
>>>
>>> model.similarity(‘A00001/B00001/C00001’, ‘A00001/B00001’)
0.21759983914124154
>>>
>>> model.similarity(‘A00001/B00001’,’A00001’)
0.067202490397546139
```


