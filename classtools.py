"""
Смешанные утилиты и инструменты классов
"""
class AttrDisplay:
    """
    Предоставляет наследуемый метод перегрузки отображения,
    который показывает экземпляры с их именами классов и пары имя=значение для каждого атрибута,
    сохраненного в самом экземпляре (но не атрибутов, унаследованных от его класснов).
    Может соединяться с любым классом и будет работать на любом экземпляре.
    """
    def gatherAttrs(self):  # Собирает атрибуты экземпляра в список
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[{}: {}]'.format(self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    x, y = TopTest(), SubTest()
    print(x)
    print(y)