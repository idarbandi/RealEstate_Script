class Manager:
    def __init__(self , _class=None):
        self._class = _class


    def search(self,**kwargs):
        results = set()
        if len(kwargs.items())==2 or 1:
            srch = kwargs.items()
            for key, value in srch:
                if key.endswith('__min'):
                    key = key[:-5]
                    compare_key = 'min'
                elif key.endswith('__max'):
                    key = key[:-5]
                    compare_key = 'max'
                else:
                    compare_key = 'equal'

                for obj in self._class.objects_list:
                    if hasattr(obj, key):
                        if compare_key == 'min':
                            result = bool(getattr(obj, key) >= value)
                        elif compare_key == 'max':
                            result = bool(getattr(obj, key) <= value)
                        else:
                            result = bool(getattr(obj, key) == value)

                        if result:
                            results.add(obj)
            return results

    def counter(self):
       return len(self._class.objects_list)
