# i18n 是什麼?
其實這個名字來自於 internationalization
字母 i 與 n 中間共有18的字母
也就是國際化的意思。  
要在 Django 使用 i18n 需要經過幾個步驟，
要使用翻譯的字詞同樣也需要相應的 TAG 或語法。  
此處使用 Django 2.2 版本作為範例，
不同版本的 Django 各有差異需要特別注意。  
首先要到 settings 確認下列這些設定值是否正確

LANGUAGE_CODE = ‘zh-Hant’  
USE_I18N = True  
USE_L10N = True  
LOCALE_PATHS = [os.path.join(BASE_DIR, ‘locale’)]  
USE_TZ = True  

[閱讀更詳細內容請點擊此處](https://blog.twshop.asia/django-%e5%a4%9a%e8%aa%9e%e8%a8%80-i18n-%e7%af%84%e4%be%8b%e6%95%99%e5%ad%b8/)
