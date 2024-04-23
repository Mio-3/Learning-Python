import string

m = """"\
$name 様

いつもお世話になっております。makioです。

$contents

以上、よろしくお願いいたします。
"""

t = string.Template(m)
mail_text = t.substitute(name=input(), contents=input())
print(mail_text)