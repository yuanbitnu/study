##模式rb 和 wb 代表对二进制文件的读写.(图片,声音,视频等以二进制文件存储)

##从一个位置copy一张图片到另一个位置
# with open('timg.jpg',mode = 'rb') as source_img_stream,\
# 	open('timg_copy.jpg',mode = 'wb') as des_img_stream:
# 	for line in source_img_stream:
# 		des_img_stream.write(line)
# 		des_img_stream.flush()