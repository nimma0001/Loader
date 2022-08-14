#getting data server
#downloading yt-playlist 480,720,1080
mkdir -p ytplaylist
echo downloading 480p
yt-dlp -f 'bv*[height=480]+ba' $1 -P ytplaylist -o '%(title)s%(resolution)s.%(ext)s'
#uplpading 480p
cd ytplaylist && find *.* | sed ':g' > playlist.txt && cd
input="ytplaylist/playlist.txt"
echo uploading 480p
while IFS= read -r line
do
  echo "ytplaylist/$line"
  #uploading to gofile
  curl https://pixeldrain.com/api/file/ -u:8e312a99-f6af-4e4d-bd43-04721db3fb61 --upload-file "ytplaylist/$line"; \
done < "$input"
rm -rf ytplaylist/*
echo "done 480p"
#uploading 720p
echo downloading 720p
yt-dlp -f 'bv*[height=720]+ba' $1 -P ytplaylist -o '%(title)s%(resolution)s.%(ext)s'
cd ytplaylist && find *.* | sed ':g' > playlist.txt && cd
input="ytplaylist/playlist.txt"
echo uploading 720p
while IFS= read -r line
do
  echo "ytplaylist/$line"
  #uploading to gofile
  curl https://pixeldrain.com/api/file/ -u:8e312a99-f6af-4e4d-bd43-04721db3fb61 --upload-file "ytplaylist/$line"; \
done < "$input"
rm -rf ytplaylist/*
echo "done 720p"
#uploadong 1080p
echo downloading 1080p videos
yt-dlp -f 'bv*[height=1080]+ba' $1 -P ytplaylist -o '%(title)s%(resolution)s.%(ext)s'
cd ytplaylist && find *.* | sed ':g' > playlist.txt && cd
input="ytplaylist/playlist.txt"
echo uploading 1080p
while IFS= read -r line
do
  echo "ytplaylist/$line"
  #uploading to gofile
  curl https://pixeldrain.com/api/file/ -u:8e312a99-f6af-4e4d-bd43-04721db3fb61 --upload-file "ytplaylist/$line"; \
done < "$input"
rm -rf ytplaylist/*
echo "Done 1080p "
#starting loop for uploading
