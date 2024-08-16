[app]
title = TaxApp
package.name = taxapp
package.domain = org.taxapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
osx.python_version =3.7.6
osx.kivy_version=1.9.1
version = 0.1
requirements = python3==3.7.6,hostpython3==3.7.6,kivy,pillow
android.sdk_path= C:\Users\rukma\Documents\TaxApp
andorid.ndk_path= C:\Users\rukma\Documents\TaxApp

[buildozer]
# (other configurations)
target = android
android.arch = armeabi-v7a
android.ndk = 21b
