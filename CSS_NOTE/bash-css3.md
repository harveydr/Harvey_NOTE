# 选择器

- DOM选择器：类选择器(class selectors)、类型选择器(type selectors)、属性选择器(attribute selectors)。
- 伪选择器

## 开始子串属性值选择器

> E[ attr ^= 'value' ]{ }

```css
a[title^='image']{}
a[href^='https']{}
a[href^='mailto']{}
a[href^='ftp']{}
```

## 结束子串属性值选择器

> E[attr $= 'value']{ }

```css
a[title$='library']{}
a[href$='.pdf']{}
a[href$='.doc']{}
```

## 任意子串属性值选择器

> E[attr *= 'value']{ }

```css
a[title*='image']{}
a[href*='.pdf']{}
```

## 多属性选择器

```css
a[href^='http://'][href*='/folder2/'][href$='.pdf']{}
```

# 连结符

