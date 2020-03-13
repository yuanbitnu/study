from setuptools import setup, find_packages

setup(
    name='smczxx',	#包名
    version='0.0.1',	#版本信息
    description='ukeyMnageSystem',
    author='tyb',
    author_email='2049008850@qq.com',
    packages= find_packages(),	#要(include)打包（exclude不要打包）的项目文件夹
    package_data = {
    },
    scripts=[],
    zip_safe=False,	# 设定项目包为不安全，需要每次都检测其安全性
    include_package_data=True,	# 自动打包文件夹内所有数据
)