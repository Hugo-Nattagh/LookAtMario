# LookAtMario

### Deep Learning - Recognizing Mario With TensorFlow

Mario being the most versatile video game character (boxing referee, motocross rider, doctor...), I thought it would be interesting to try to see how deep learning would recognize him over more than 30 years. 

#### What's going on

I used **TensorFlow's faster R-CNN**. Faster R-CNN is a 2 step process for each frame.  
First, the region proposal: all potential regions of interest (ROI) are selected with bounding boxes.  
Then, features inside of those boxes are analyzed to perform classification. 

![](https://github.com/Hugo-Nattagh/LookAtMario/blob/master/mario_gif.gif)

#### Thank you

I was strongly inspired by [sentdex](https://www.youtube.com/playlist?list=PLQVvvaa0QuDcNK5GeCQnxYnSSaar2tpku) video series, and followed most of the steps he gave in them.  
I used the work of [datitran](https://github.com/datitran/raccoon_dataset) (`convert-xml-csv.py` and `gen-tfrecord.py`).  
I also used `labelImg.exe` from [tzutalin's repo](https://github.com/tzutalin/labelImg).

#### But why?

This project was done for me to get familiar with object detection using TensorFlow, I can't really say I pushed the envelope.  
But it was fun to work on it and the result was satisfying even though there is much room for improvement. I'm not done with it yet! 

#### Files Description

- `convert-xml-csv.py`: Convert all the manually set labels to a csv file
- `gen-tfrecord.py`: Generate a tfrecord file from a csv file
- `train.py`: Where the magic happen, train the model
- `export_inference_graph.py`: Export the model
- `vid-detect.py`: Extract frames from a video and save them with labeled bounding boxes
- `create_vid2.py`: Recreate video from frames
