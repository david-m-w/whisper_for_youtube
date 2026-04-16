# Sind Sie von der P5 (ABITUR) hier?
Da dieses Dokument (der Code und die Dokumentaton hier) nur ein Werkzeug ist, sollte es nicht zur Bewertung der P5 genuztz werden, sondern nur zum Verständniss, wo ich den Text aus dem Video habe (der hier als Beispiel in `transcript.txt` ist, damit sie den code nicht selber ausführen müssen). Durch mehrere Stichproben (Originalvideo mit erkanntem text vergleichen) habe ich entschieden, dass dieses Programm alles erfasst ohne ganze Sätze zu überspringen (maximal einzelne Wörter die sich aus dem Kontext erübrigen), und daher ein passender Ersatz für das Video ist.

# what is this
AI generated quick script for getting transcripts of youtube videos when no closed captions are available.
basically a wrapper for whisper

# requirements
Designed for cuda

# potential features
maybe i add a batching thing, so that it cna do it in paralell
it would have to let you choose how long the clips are each.

also maybe a silence fixer, if the model halucinates during silences
from the extensive testing ive done (one 5h video, trust me bro, one test is probably very representative of the average video) it seems like there defintly are some problems with whisper halucinating reetitions, buts it dosent seem to actually skip content, its just once in a while that theres 10-15 words you have to skip.
sadly this also seems to happen when its loud/not very understandable, so idk if a silence skipper can do the job, havent looked into this stuff.

# why only for non cc videos?
if they are, this will also work, but its easier and dosent require compute to jut download the transcript from a transcriptwebsite (youtubettt.com for example)

# errors i found but cant be botherd debugging:
first time i ran it with medium mdel it gave this error:

`
Error downloading audio: ERROR: [generic] ' source /home/[...]/.venv/bin/activate\rhttps://www.youtube.com/watch?v=pXq-5L2ghhg' is not a valid URL
`