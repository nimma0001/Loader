#getting data server
curl https://api.gofile.io/getServer > out.json
serv="$(jq -r '.data.server' out.json)"
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
  curl -F folderId=6360ad17-a0aa-4eb1-9c10-09ea9512da63 -F token=oW4ByRUjVR0BWejW1UY4fsagfRSedgLk -F file=@"ytplaylist/$line" https://$serv.gofile.io/uploadFile
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
  curl -F folderId=ec36a95d-fb25-489c-ab70-70bcf08cdbd5 -F token=oW4ByRUjVR0BWejW1UY4fsagfRSedgLk -F file=@"ytplaylist/$line" https://$serv.gofile.io/uploadFile
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
  curl -F folderId=c21ef52c-ac28-4322-a4fa-7d9224490b79 -F token=oW4ByRUjVR0BWejW1UY4fsagfRSedgLk -F file=@"ytplaylist/$line" https://$serv.gofile.io/uploadFile
done < "$input"
rm -rf ytplaylist/*
echo "Done 1080p "
#starting loop for uploading
