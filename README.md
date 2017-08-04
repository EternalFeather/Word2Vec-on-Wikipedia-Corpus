Word2Vec on Wikipedia
===
我们知道语言在人际交往当中充当了重要的角色，理解语言的编码就能够了解对方所要表达的意思。而机器不同于人，无法从繁杂的文字当中快速提取有用的信息，因此需要借助一个能够代表文字语言的编码单位，也就是我们说的**向量（Vector）**。因此训练Word2Vec的模型，用来计算词语之间的相似度似乎成为了解决文字编码问题的不可或缺的重要途径之一。

# 配置需求

- `Python3`
- `Gensim` >= 2.3.0 (**沒試過更低的版本**)
- `Opencc`
- `jieba`

# 模型训练语料
- 维基百科官方提供了大约11G的很好的英文語料： [開源數據鏈接](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)。
- 同時也提供了大約1.5G的中文語料： [開源數據鏈接](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)。

其主要的文档格式以 `.xml` 为主。

# 操作流程

## 資料前處理
前處理第一階段需要將wiki的 `.xml` 格式的數據轉換成 `text` 格式的數據:
- 通過 `word2vec_process.py` 實現，基本參數包括：

    - `-data`： 輸入的維基百科數據集。
    - `-output`： 輸出的文件位置和名稱。
```
python word2vec_process.py -data enwiki-latest-pages-articles.xml.bz2 -output wiki.en.text
```

**Tips:** 
- 如果是中文維基百科的語料訓練時，會存在一些繁體和簡體混雜的中文字，如果想要統一字體格式，就可以使用Opencc將字體進行轉換：

```
opencc -i wiki.zh.text -o wiki.zh.text.jianti -c zht2zhs.ini
```
- 中文的維基百科數據接下來就是需要進行斷詞處理了，這裏使用的**中文斷詞工具**是 `jieba`。

這裏利用了gensim裏面處理維基百科的class `WikiCorpus`，通過 `get_texts` function將每篇文章換行輸出成text文本，並且已經完成了去標點的工作。運行之後就能夠得到英文維基百科的數據文檔 `wiki.en.text`(參數可自行設定名稱)。

## 模型訓練
有了文章的text數據集之後，無論是word2vec binary版本還是gensim的word2vec，都可以用來訓練我們的模型，不過後者的運算速度比較快。

- 模型的建立通過 `word2vec_model.py` 實現，基本參數包括：

    - `-text`： 輸入的維基百科文字檔名稱。
    - `-vector`： 輸出的向量文檔存儲位置和名稱（默認爲 **wiki.en.text.vector**）。
    - `-core`： 多進程運行使用的cpu數量（默認爲全部）。

```
python word2vec_model.py -text wiki.en.text -vector wiki.en.text.vector -core 8
```

## 模型測試
訓練結束之後就能得到一個gensim原始c版本的word2vec的vector格式的模型，這時候我們就可以利用這些模型進行一些文字的評估測試了：

- 導入模型進行操作通過 `word2vec_eval.py` 實現，基本參數包括：

    - `-vector`： 載入的模型位置和名稱。
    - `-mode`： 想要執行模型的功能名稱（包括 *similar**【預測相關的words】、**similarity**【判斷兩個words的相似度】等）

```
python word2vec_eval.py -vector wiki.en.text.vector -mode similarity
```

# Reference
[我愛自然語言處理](http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C)

# KeyWords

###### Tags: `Word2Vec` `Embedding`
