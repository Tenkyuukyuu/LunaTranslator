from qtsymbols import *
from rendertext.internal.webview.base import base, datas


class TextLine(base):

    def gen_html(self, text, data: datas):
        _id = self.getuid()

        style = f"""#{_id}{{
            {self.fontinfo}
            color:{data.color}; 
            {self.align}
            {self.line_height}
        }}
        """
        return self.makedivstyle(_id, text, style)
