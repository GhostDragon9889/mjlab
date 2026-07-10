volume_path="/project/dockerVolm/local_wandb"
port="6010"
wan_ip="0.0.0.0"
container_name="wandb-container"
image_name="wandb/local"
# Expiration in 12 months
LICENSE_KEY="eyJhbGciOiJSUzI1NiIsImtpZCI6InUzaHgyQjQyQWhEUXM1M0xQY09yNnZhaTdoSlduYnF1bT
RZTlZWd1VwSWM9In0.eyJjb25jdXJyZW50QWdlbnRzIjoxLCJ0cmlhbCI6ZmFsc2UsIm1heFN0b3JhZ2VHYiI6MTAsIm1heFRlYW1z
IjowLCJtYXhVc2VycyI6MSwibWF4Vmlld09ubHlVc2VycyI6MCwibWF4UmVnaXN0ZXJlZE1vZGVscyI6MiwiZXhwaXJlc0F0IjoiMjAyNy0wNy0xMFQ
wNDo0NTowNS4xOThaIiwiZGVwbG95bWVudElkIjoiZjk4MmRkZGYtNzA4OC00NTc5LThiNzYtM2IzNjU0Yzg5OTFjIiwiZmxhZ3MiOltdLCJjb250cmFjdFN
0YXJ0RGF0ZSI6IjIwMjYtMDctMTBUMDQ6NDU6MDUuMTk5WiIsImFjY2Vzc0tleSI6IjM1OWQ0OWJhLTBhOWQtNGE2NC1iZWYwLWZiYjk1M2VmOTBjNyIsInNlYXR
zIjoxLCJ2aWV3T25seVNlYXRzIjowLCJ0ZWFtcyI6MCwicmVnaXN0ZXJlZE1vZGVscyI6Miwic3RvcmFnZUdpZ3MiOjEwLCJleHAiOjE4MTUxOTQ3MDUsIndlYXZlT
GltaXRzIjp7IndlYXZlTGltaXRCeXRlcyI6bnVsbCwid2VhdmVPdmVyYWdlQ29zdENlbnRzIjowLCJ3ZWF2ZU92ZXJhZ2VVbml0IjoiTUIifX0.oKzghhuc3vdzmmOi
E0EDTofP0SIHgSsQrQTdQiB_obSHMb7I4XaROZ7oLXoNPm8MwHL3FZ6FiqbtiPFh0Iw6J7jj3ImUQiGXct7PGbcqoKeDNDwiAhZHYmbL1uKIHBFt6ZPW3Ft3TJzYXAu6
8M__0gh3H37xKb6UwF-yV20HOEn3RiV3MC7qzQPd6wCpeYO562mqo_XuL1faojBl8Cort4XCFcWM2Xstxb_y2uoM6-tyZ0zxVP0U8da_m90j2nz8BmktAmf2PTjEWs_PQ
b31518sMvcSkOMG1Jnm3AOoD3XhQpZ_RUOhs_ZbhlgQDRuNvO5AOCem4P9GOLqEwIAUBg"

sudo docker run --name "$container_name" \
  -e LICENSE="$LICENSE_KEY" \
  -e TZ=Asia/Shanghai \
  -v "$volume_path":/vol \
  -e "HOST=http://$wan_ip:$port" \
  -p "$port":8080 \
  --restart always \
  -d "$image_name"


# docker run --rm -d \
# 	-e HOST=http://$wan_ip:6010 \
# 	-p 6010:8080 \
# 	-v /path/on/host:/vol \
# 	--name wandb-local \
# 	wandb/local


#https://blog.csdn.net/qq_49030008/article/details/146548003
#https://blog.csdn.net/ever_____/article/details/151334123