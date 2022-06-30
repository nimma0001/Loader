echo "$1 uploading pixel"; \
curl -T "$1" -u :"011ac321-1c21-4aa0-8608-ea69c55fa7ea" https://pixeldrain.com/api/file/; \
echo "$1 uploaded pixel drain"; \
echo "$1 UPLOADING onedrive"; \
rclone copy /app/"$1" one:Public/July/"$2"; \
echo "$1 uploaded onedrive"; \
echo "script complete"
