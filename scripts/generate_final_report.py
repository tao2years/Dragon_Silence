from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, HRFlowable,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "龙息神寂_370区_S1_Day1最终策略报告.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

FONT = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
pdfmetrics.registerFont(TTFont("YaHei", FONT))
pdfmetrics.registerFont(TTFont("YaHei-Bold", FONT_BOLD))

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#172235")
INK = colors.HexColor("#263247")
MUTED = colors.HexColor("#667085")
TEAL = colors.HexColor("#197C78")
TEAL_LIGHT = colors.HexColor("#E8F5F3")
AMBER = colors.HexColor("#A85E00")
AMBER_LIGHT = colors.HexColor("#FFF4DF")
RED = colors.HexColor("#B42318")
RED_LIGHT = colors.HexColor("#FEECEB")
BLUE_LIGHT = colors.HexColor("#EDF4FF")
LINE = colors.HexColor("#D8DEE8")


class ReportDoc(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(
            str(path), pagesize=A4,
            leftMargin=16 * mm, rightMargin=16 * mm,
            topMargin=18 * mm, bottomMargin=16 * mm,
            title="龙息神寂 370区 S1 Day1 最终策略报告",
            author="Codex research project",
            subject="370区抽卡、火毒路线、首周副本与赛季规划",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=self.decorate))

    def decorate(self, canvas, doc):
        canvas.saveState()
        page_num = canvas.getPageNumber()
        canvas.setFont("YaHei", 7.6)
        canvas.setFillColor(MUTED)
        canvas.drawString(16 * mm, 8 * mm, "证据等级：官方/客户端 > 可复现队伍码 > 社区样本 > 研究推断")
        canvas.drawRightString(PAGE_W - 16 * mm, 8 * mm, f"{page_num}")
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CN", fontName="YaHei", fontSize=9.2, leading=14.0,
                          textColor=INK, spaceAfter=4.5))
styles.add(ParagraphStyle(name="SmallCN", fontName="YaHei", fontSize=7.6, leading=11.2,
                          textColor=INK, spaceAfter=2.5))
styles.add(ParagraphStyle(name="Tiny", fontName="YaHei", fontSize=6.8, leading=9.7,
                          textColor=MUTED))
styles.add(ParagraphStyle(name="H1CN", fontName="YaHei-Bold", fontSize=17, leading=23,
                          textColor=NAVY, spaceBefore=2, spaceAfter=9))
styles.add(ParagraphStyle(name="H2CN", fontName="YaHei-Bold", fontSize=11.5, leading=16,
                          textColor=TEAL, spaceBefore=7, spaceAfter=5))
styles.add(ParagraphStyle(name="H3CN", fontName="YaHei-Bold", fontSize=9.4, leading=13,
                          textColor=NAVY, spaceBefore=5, spaceAfter=3))
styles.add(ParagraphStyle(name="BulletCN", fontName="YaHei", fontSize=8.8, leading=13.2,
                          leftIndent=12, firstLineIndent=-8, bulletIndent=3, textColor=INK,
                          spaceAfter=2.5))
styles.add(ParagraphStyle(name="CoverTitle", fontName="YaHei-Bold", fontSize=27, leading=35,
                          textColor=NAVY, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="CoverSub", fontName="YaHei", fontSize=12, leading=19,
                          textColor=TEAL))
styles.add(ParagraphStyle(name="Decision", fontName="YaHei-Bold", fontSize=13, leading=19,
                          textColor=RED, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="Callout", fontName="YaHei", fontSize=9.2, leading=14.2,
                          textColor=INK, leftIndent=7, rightIndent=7, spaceAfter=2))
styles.add(ParagraphStyle(name="Table", fontName="YaHei", fontSize=7.1, leading=10.2,
                          textColor=INK))
styles.add(ParagraphStyle(name="TableHead", fontName="YaHei-Bold", fontSize=7.2, leading=10.4,
                          textColor=colors.white, alignment=TA_CENTER))


def P(text, style="CN"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph("- " + text, styles["BulletCN"])


def box(text, bg=TEAL_LIGHT, border=TEAL, style="Callout"):
    t = Table([[P(text, style)]], colWidths=[177 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.8, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def table(headers, rows, widths, font=7.1):
    data = [[P(str(x), "TableHead") for x in headers]]
    for row in rows:
        data.append([Paragraph(str(x), ParagraphStyle(
            name=f"cell{font}", parent=styles["Table"], fontSize=font, leading=font + 3.0
        )) for x in row])
    t = Table(data, colWidths=[w * mm for w in widths], repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FC")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


story = []

# Cover
story += [Spacer(1, 20 * mm), P("龙息神寂", "CoverSub"), Spacer(1, 3 * mm),
          P("370区 S1 Day1<br/>最终策略报告", "CoverTitle"), Spacer(1, 8 * mm),
          HRFlowable(width="100%", thickness=2, color=TEAL, spaceAfter=8 * mm),
          P("开服日期：2026-10-22　|　当前：S1 第1天　|　偏好：火 / 毒伤", "CoverSub"),
          Spacer(1, 12 * mm),
          box("<b>最终结论</b><br/><font color='#B42318'><b>当前腐蚀精选召唤III：0抽。完整保留300抽。</b></font><br/>主规划走现代毒伤；燃烧作为第二项目。任何卡池在客户端确认候选、里程碑和独立累计规则前，不投入试抽。", RED_LIGHT, RED),
          Spacer(1, 8 * mm),
          P("这份报告不是资料堆砌，而是一套可直接照做的决策顺序：今天做什么、300抽如何选、队伍怎么搭、副本卡住怎么换人、后续何时重新评估。", "CN"),
          Spacer(1, 18 * mm),
          P("研究库版本：Pass 66　|　160个来源ID　|　77份Markdown　|　113条本地链接已校验", "SmallCN"),
          P("重要边界：尚未取得370客户端卡盒、当前池完整规则、世界日历和榜单截图；文中所有未实测内容均明确标注。", "SmallCN"),
          PageBreak()]

# Executive
story += [P("1. 一页执行摘要", "H1CN"),
          box("<b>今天的唯一抽卡动作：不抽。</b> 腐蚀队需要毒龙、卢克、城主/挂腐蚀位、雷塔/辅助和生存壳，低投资或短战未必优于成熟火毒队；而且历史官方规则显示不同限时池累计独立、结束清零，试抽不能给下一池垫进度。", AMBER_LIGHT, AMBER),
          P("账号总路线", "H2CN"),
          table(["优先级", "项目", "成立条件", "当前动作"], [
              ["1", "现代毒伤", "心愿/溯影候选中出现蛇女，且欧勾克、图奇等可在较低里程取得", "准备300；候选确认后按100/200/300拿核心"],
              ["2", "现代燃烧", "派克西顿 + 卡尔弗 + 杜瑞姆/火拳能够形成铺火、结算、生存闭环", "先观察组件，不为单卡建队"],
              ["3", "旧毒伤", "已有子夜或斯赖特之一，且有图奇/杜兰戈挂毒与欧勾克生存", "仅在现代毒伤不可选时考虑"],
              ["4", "龙妈狂野", "龙妈 + 菲莉丝蒂/可拉克等狂野发动机到位，且愿意投入激励/专属", "喜欢可以留，但不做第一周主项目"],
              ["跳过", "当前腐蚀", "除非改变偏好并愿意长期补全高成本骨架", "0抽"],
          ], [13, 28, 92, 44]),
          P("Day1结束前", "H2CN"),
          bullet("只养一队5人：可靠前排 + 治疗/护盾 + 范围减益 + 主输出 + 副输出/机制位。"),
          bullet("主线推进到自然锁级；地精打到稳定三星最高层；剧毒墓穴拿首通；最后用最新等级再打海王。"),
          bullet("海王先用1坦 + 2辅助 + 2单体输出；每次只换一人，记录总伤害、战斗时长、首个阵亡和阵亡时间。"),
          bullet("截图5项：卡盒、腐蚀池详情/累计、溯影六候选、世界日历、海王技能与榜单。"),
          bullet("在客户端尝试导入毒伤队伍码：S9261020QU5B7BX2（有子夜）与 S9261020QU7AO4B3（无子夜）。当前状态仅为公开码，尚未在370验证。"),
          P("本次研究真正修正了什么", "H2CN"),
          bullet("纠正“300抽拿两个古早主C”：同结构官方模板中，300拿第一名稀有输出，第二名在800。"),
          bullet("纠正S7卡池漏项：最后精选到自选是9天；S8是15天，因此S9只设10月31日-11月8日监控窗，不冒充确定轮换。"),
          bullet("把寰空远征从模糊预测收口为Day37-50 + 共鸣80 + 本服预告。"),
          bullet("把“天使11月8日”拆为历史确有返场、但具体日期仍是社区说法；不据此抽卡。"),
          PageBreak()]

# 300 pulls
story += [P("2. 300抽决策树", "H1CN"),
          box("<b>先确认池型，再谈目标。</b> 预言召唤3.0、六格心愿/溯影、当前腐蚀精选III是三个独立系统；它们的结果、里程碑和累计不能混算。", BLUE_LIGHT, colors.HexColor("#4672B4")),
          P("第一选择：现代毒伤", "H2CN"),
          table(["你的卡盒", "100档", "200档", "300档", "结论"], [
              ["四人都没有", "欧勾克", "图奇", "蛇女", "300即停；后续补斯赖特/杜兰戈/机制位"],
              ["已有欧勾克", "图奇", "杜兰戈或通用坦辅", "蛇女", "300即停"],
              ["已有图奇", "欧勾克", "杜兰戈或通用坦辅", "蛇女", "300即停"],
              ["已有蛇女", "欧勾克", "图奇", "斯赖特", "若候选可用则300停"],
              ["已有蛇女+斯赖特", "欧勾克", "图奇", "第二体系主C", "候选无明确价值则整池跳过"],
          ], [37, 30, 47, 30, 33]),
          P("可用五人骨架：<b>蛇女 + 图奇/杜兰戈 + 欧勾克 + 可靠前排 + 破防/降攻/驱散位</b>。拿到斯赖特后，再替换挂毒或机制位。斯赖特是上限件，不是蛇女队开机门票。", "CN"),
          P("若蛇女不在候选", "H2CN"),
          table(["条件", "建议"], [
              ["已有斯赖特，且有图奇/杜兰戈", "300可选子夜；100/200补欧勾克和挂毒/坦辅"],
              ["已有子夜，且有挂毒手", "300可选斯赖特；100/200补欧勾克和图奇/杜兰戈"],
              ["子夜、斯赖特都没有", "300只能拿其中一个，不算闭环；默认不立项"],
              ["连图奇/杜兰戈也没有", "旧毒伤启动慢且组件缺口大；跳过"],
          ], [70, 107]),
          P("火系和古早主C怎么选", "H2CN"),
          table(["路线", "最低开机条件", "不该做的事"], [
              ["燃烧", "派克西顿 + 卡尔弗 + 杜瑞姆/火拳；按Boss让杜瑞姆与火拳换位", "把火拳+卡尔弗+杜瑞姆写成无条件毕业队"],
              ["狂野龙妈", "龙妈 + 菲莉丝蒂/可拉克等狂野发动机 + 生存壳", "只拿龙妈一张就投入全部资源"],
              ["冰龙/鸟姐/暗龙/光领主", "分别偏群怪、海王单体、长战召唤、鼓舞；需对应组件", "按宣传图选两张主C，第一周同时拉两队"],
          ], [29, 91, 57]),
          box("<b>双目标原则：</b>先拿一套能立即工作的主线，再选第二队主C。不要选两张都需要昂贵专属组件的输出。六候选界面未看到前，不最终落笔。", AMBER_LIGHT, AMBER),
          PageBreak()]

# Day1 sequence
story += [P("3. Day1逐步作战清单", "H1CN"),
          P("推荐顺序", "H2CN"),
          table(["阶段", "动作", "完成标准"], [
              ["上线第一轮", "推主线；新玩法各首通一次；加入活跃盟会；旅程商店检查未拥有英雄", "自然锁级前不刷低层资源本"],
              ["第一次锁级", "地精据点手动打到当前稳定三星最高层；只补主力蓝/紫装", "新层能过即停止刷旧层"],
              ["装备首通", "剧毒墓穴优先；保留群攻给复活的小怪", "拿首通和可用过渡装，不追完美词条"],
              ["海王摸底", "A档3生存 -> B档2生存 -> C档短爆发；每档连续3次", "以奖励档和稳定性为先，不只看单次峰值"],
              ["下线前", "清100活跃、竞技免费次数、迷域、委托、红点；用最新等级重打海王", "记录资源和五张关键截图"],
          ], [25, 102, 50]),
          P("养成优先级", "H2CN"),
          table(["顺序", "资源投向", "理由"], [
              ["1", "主坦生存", "主坦倒下会直接结束多数Boss尝试"],
              ["2", "治疗/护盾/降攻", "让输出曲线延长，首日常比多上一名C更有效"],
              ["3", "关键命中", "保证降攻、破防、挂毒等机制生效；不同Boss需重新测"],
              ["4", "主输出", "技能等级优先投能改变循环或覆盖率的节点"],
              ["5", "副输出/工具人", "先达到能穿装和放关键技能的最低等级"],
          ], [14, 67, 96]),
          P("海王A/B/C递进", "H2CN"),
          table(["档", "阵容", "何时进入下一档", "记录"], [
              ["A 生存基线", "最高生命主坦 + 治疗 + 护盾/降攻 + 2单体输出", "3次都稳定活到后段", "总伤、秒数、首死、退场原因"],
              ["B 默认", "主坦 + 2辅助 + 2输出", "换掉最弱生存位后，平均总伤上升且不早死", "同上，至少3次"],
              ["C 短爆发", "主坦 + 1辅助 + 3输出，或极限4输出", "只用于冲下一奖励档；早死就退回B", "不要用单次暴击样本下结论"],
          ], [25, 59, 63, 30]),
          P("历史官方蓝紫海王赛果同时出现9分钟双生存17M和5分钟四输出12.82M，说明首日答案取决于生存曲线，不是辅助越少越好。该数字是机制样本，不是370目标线。", "SmallCN"),
          PageBreak()]

# Dungeon cheat sheet
story += [P("4. 副本阵容与失败排查", "H1CN"),
          table(["副本", "起测阵容", "关键动作", "失败时只改一项"], [
              ["地精据点", "范围减益 + 西格莉德 + 2群攻 + 聚怪/收尾", "先减益再触发西格莉德；两组威能轮换，不在残血波浪费", "差几秒：改自动时序；清不动：提高主C而非平均抬十人"],
              ["剧毒墓穴", "坦 + 治疗 + AoE/减益 + 单体 + 机制位", "先杀四磷火；Boss复活后用预留AoE再清", "小怪活太久：加AoE；Boss压不动：换单体/破防"],
              ["诅咒墓穴", "坦 + 群盾 + 敌方增益移除 + 降攻 + 输出", "历史6/12/18秒轴仅作起点；盾住吸血/生命上限损失", "Boss回血：查驱散；暴毙：查盾时序和降攻覆盖"],
              ["腐烂墓穴", "坦 + 治疗 + 免疫/净化 + 单体 + 机制位", "Boss按减益数量强化；分散站位，避免无意义叠毒/寒霜", "关键减益被挤掉：删次要状态；治疗崩：补免疫/净化"],
              ["天赋本", "按机制带免疫/控制/驱散，而非追亲和", "必要时关自动，手操关键技能", "只换对应机制位，不重做整队"],
          ], [25, 47, 66, 39], font=6.8),
          P("火毒在副本中的正确用法", "H2CN"),
          bullet("毒伤：需要持续挂毒链和稳定生存，适合长战；在限制减益数量或频繁净化的Boss前先验证，不要默认克制一切。"),
          bullet("燃烧：必须同时解决铺火、爆燃/焚毁结算和生存。燃烧也可能占用Boss状态槽，关键破防/降攻被覆盖时应删掉低价值状态。"),
          bullet("龙妈：缺狂野组件时只当单体C比较，不把成熟榜单队当Day1门槛。"),
          P("通用换人逻辑", "H2CN"),
          table(["症状", "优先检查", "换人方向"], [
              ["主坦最先死", "生命是否全队最高、降攻是否覆盖、治疗是否提前交", "加盾/降攻，不先加第三输出"],
              ["全队同时倒", "Boss大招机制、站位、免疫/净化窗口", "补机制辅助或分散"],
              ["活着但伤害低", "破防/削抗、循环、技能空放、状态被覆盖", "先修轴，再换输出"],
              ["偶尔过、经常不过", "命中、暴击随机、首死时间波动", "连续3次取中位数，稳定后再升级"],
          ], [39, 83, 55]),
          PageBreak()]

# Timeline
story += [P("5. S1开放节奏与资源计划", "H1CN"),
          box("370同时受两只时钟影响：<b>新手赛季玩法按服务器日推进</b>；<b>2026部分召唤活动按全服日历同步</b>。所以370看到S9腐蚀池，不代表玩法跳过S1，也不能用旧服Day13池推算下一池。", BLUE_LIGHT, colors.HexColor("#4672B4")),
          table(["时间", "规划节点", "370条件日期/动作", "证据强度"], [
              ["Day1-7", "主队、地精、墓穴、海王、资源核账", "10月22日-28日；每天记录真实骰子和龙髓", "官方新手指南 + 历史强基线"],
              ["Day10-30", "检查心愿/追赶池资格", "10月31日-11月21日；只检查，不预设必开", "普通服/庆典服社区样本分歧"],
              ["Day22", "大陆挑战/先祖遗迹无尽节点", "11月12日前准备至少两套功能骨架", "官方S1基线"],
              ["Day23-26", "盟会战窗口", "11月13日-16日；保持活跃盟会", "官方S1基线"],
              ["Day37-50", "寰空远征分批开放，共鸣80", "11月27日-12月10日看本服预告", "官方窗口，精确日待客户端"],
              ["Day42", "异界前置任务", "12月2日前补齐驱散/免疫/多队工具人", "官方基线"],
              ["Day54", "复苏之龙", "12月14日前准备多队与每日次数规划", "2026新手季正文直接确认"],
              ["约Day70", "赛季结算", "约12月30日；以370世界日历为准", "历史赛季结构"],
          ], [21, 50, 66, 40], font=6.8),
          P("资源纪律", "H2CN"),
          bullet("官方“首周110+抽”是多资源宣传口径，不等于110个可投入目标限时池的橙骰。"),
          bullet("日芒、龙髓、池专用免费抽、昨日结算和历史过期福利必须分栏；Day7做第一次300抽可达性审计。"),
          bullet("预言召唤3.0的260次是端外试刷，锁定未来真实100次日芒结果；周年30次免费日芒已于2026-04-19结束，370默认不计入。"),
          bullet("任何“先垫几十抽”都必须先证明累计继承；现有官方历史证据恰好相反：不同限时活动独立累计、结束清零。"),
          PageBreak()]

# Banner forecast
story += [P("6. 后续卡池：能推测什么，不能推测什么", "H1CN"),
          P("可执行预测", "H2CN"),
          table(["观察点", "依据", "结论"], [
              ["10月31日", "S7最后精选到自选为9天；也是370 Day10", "同时检查全服下一池和370追赶/心愿资格"],
              ["11月6日", "S8最后精选到自选为15天", "作为较晚对照点，不是官宣"],
              ["11月8日", "社区称天使返场", "只在出现官方活动页、日期、候选、池规后升级"],
              ["11月21日", "370 Day30", "若仍无心愿入口，重新规划300抽用途"],
          ], [28, 81, 68]),
          P("天使返场的证据拆分", "H2CN"),
          bullet("官方历史事实：弥菈希亚“圣谕辉光召唤”在2026-06-26和2026-08-17均出现，间隔52天，证明角色专属池会返场。"),
          bullet("不能推出：下一次一定在11月8日。52天机械外推会落在10月8日，且只有一个间隔样本，不足以拟合规律。"),
          bullet("对本账号的影响：你走火/毒，灵光天使本身不补当前主线；即使官宣，也只有在已有昂贵灵光闭环时才重算。"),
          P("下一池五道闸门", "H2CN"),
          table(["闸门", "必须回答"], [
              ["1 池型", "是输出精选、辅助定向、角色专属，还是370追赶池？"],
              ["2 指定目标", "300里程能明确得到谁？是否只是概率普通组件？"],
              ["3 账号闭环", "抽到后能否立即组成四人核心，而不是新增一张孤立传说？"],
              ["4 替代成本", "同职能是否能在心愿100/200档或商店更便宜取得？"],
              ["5 现金流", "抽完是否仍保得住现代毒伤主C的300预算？"],
          ], [29, 148]),
          box("只要任一闸门回答为“未知”，默认停手。预测用于提高检查频率，不用于提前消费。", AMBER_LIGHT, AMBER),
          PageBreak()]

# Old server access
story += [P("7. 前区榜单、队伍码与邀请码", "H1CN"),
          P("现实可行性排序", "H2CN"),
          table(["路径", "能得到什么", "当前判断"], [
              ["370内导入公开队伍码", "五人、激励、神器、装备、技能轴的潜在快照", "成本最低；先试两条S9毒伤码"],
              ["370同联赛榜单/推荐阵容", "当前版本的真实海王、挑战赛样本", "需客户端截图；优先采榜1/10/50并记录战斗秒数"],
              ["公开视频/攻略战报", "老区成熟队与机制线索", "可作样本，版本和投资必须标注"],
              ["旧服盟会邀请码", "可能在允许建角时进入指定盟会/服务器", "公开码多为好友绑定或历史S1码；不能绕过关服注册"],
          ], [42, 80, 55]),
          P("邀请码结论", "H2CN"),
          bullet("好友绑定/庆典奖励码不等于服务器准入码。"),
          bullet("历史盟会邀请码通常需要2级盟会会长生成，可能限时、限S1；截至研究截止没有找到可验证的368/369当前有效码。"),
          bullet("如果旧服务器已禁止创建角色，公开邀请码通常不能绕过注册锁。最有效路径是用队伍码和榜单截图在370旁路复原。"),
          P("首批要采的样本", "H2CN"),
          table(["样本", "记录字段"], [
              ["海王榜1/10/50", "服务器、阵容、激励、神器、总伤、战斗秒数、估算DPS、首死时间"],
              ["大陆挑战", "Boss、阵容、关键命中/急速、手操点、剩余时间、失败原因"],
              ["队伍码", "能否解析、跨赛季是否可预览、五人、装备、技能轴、发布日"],
              ["自己的三次测试", "仅换一名角色；记录中位数，不用单次暴击峰值"],
          ], [43, 134]),
          PageBreak()]

# Today quick card
story += [P("8. 今天照着做 - 快速卡", "H1CN"),
          box("<b>抽卡：</b>腐蚀池0抽；不垫抽；不把不同池累计混算；完整保留300。", RED_LIGHT, RED),
          P("上线后", "H2CN"),
          bullet("推主线到锁级 -> 地精最高稳定三星 -> 剧毒墓穴首通 -> 回地精提升 -> 最新状态打海王。"),
          bullet("只养5名：坦、治疗/盾、减益、主C、副C/机制。额外工具人只升到能工作。"),
          bullet("海王先B档：最高生命主坦 + 2辅助 + 2单体输出；3次稳定后才减辅助。"),
          P("看到心愿/溯影时", "H2CN"),
          bullet("先截图完整六候选和100/200/300/400/600/800奖励。"),
          bullet("若蛇女在300稀有位：优先100欧勾克 -> 200图奇 -> 300蛇女，停。"),
          bullet("若蛇女不在：只有已有子夜/斯赖特之一且挂毒、生存组件足够，才走旧毒。"),
          bullet("燃烧只在派克西顿、卡尔弗、杜瑞姆/火拳能闭环时立项；龙妈只在狂野发动机到位时立项。"),
          P("今晚必须留下", "H2CN"),
          table(["项目", "记录"], [
              ["卡盒", "全部传说/史诗、激励等级、可用蓝紫机制卡"],
              ["召唤", "腐蚀池详情/累计、溯影六候选、日芒/预言入口"],
              ["进度", "共鸣等级、主线位置、地精最高三星、墓穴最高层"],
              ["海王", "技能页、榜1/10/50、自己的3次总伤/秒数/首死"],
              ["资源", "日芒骰、龙髓、池专用免费抽、已投入、兑换价"],
              ["日历", "370世界日历完整截图"],
          ], [34, 143]),
          box("拿到这些截图后，下一版不再是通用建议，而能直接输出：你现有卡盒的五人主队、每个副本替代位、技能轴、装备主属性和300抽最终落点。", TEAL_LIGHT, TEAL),
          PageBreak()]

# Evidence
story += [P("9. 证据边界与研究结论", "H1CN"),
          P("已确认", "H2CN"),
          bullet("历史官方规则：不同召唤活动累计独立、结束清零；300试抽应视为本池沉没成本。"),
          bullet("同结构六格心愿/溯影：第三、六档为稀有输出位；公开模板为100/200/300/400/600/800。"),
          bullet("S1中后期：Day22大陆挑战节点；寰空远征Day37-50、共鸣80并看本服预告；Day42前置；2026新手季正文确认Day54复苏之龙。"),
          bullet("弥菈希亚专属池曾在2026-06-26和2026-08-17两次出现，但不足以推出11月8日。"),
          P("仍需370客户端验证", "H2CN"),
          bullet("当前腐蚀精选III完整辅助名单、结束时间、首金规则、300自选页面。"),
          bullet("370属于普通新服、庆典服还是追赶服；心愿池开放日和候选范围。"),
          bullet("现有公开队伍码能否跨服务器、跨赛季解析；自己的卡盒与技能/装备实际数值。"),
          bullet("世界日历全部精确日期；368/369榜单与有效盟会邀请码。"),
          P("未做过的事", "H2CN"),
          bullet("未登录用户账号，也未进行任何付费、召唤或游戏内运行时测试。"),
          bullet("B站页面多次返回412；已恢复BV号、标题、部分评论与公开队伍码，但未把看不到的画面配置当作事实。"),
          bullet("NGA和贴吧公开检索命中不稳定；搜索不到不等于不存在，未虚报覆盖完整。"),
          P("最终判断", "H2CN"),
          box("<b>370 S1 Day1最优策略不是追当前强势标签，而是保持选择权：</b>用一支低成本功能队推进内容，完整保存300，在六候选真实出现后优先闭合现代毒伤；燃烧作为第二项目。当前腐蚀、天使传闻和旧服邀请码都不值得打断这条主线。", TEAL_LIGHT, TEAL),
          PageBreak()]

# Sources
story += [P("10. 核心来源", "H1CN"),
          P("以下仅列支撑关键结论的一手/高价值来源。研究库保留完整160项来源索引、快照状态、引用关系与纠错记录。", "CN")]

sources = [
    ("CN-OFFICIAL-009", "萌新指南｜公测第一天", "2025-03-20", "https://www.taptap.cn/moment/651751150319569831"),
    ("CN-OFFICIAL-033", "龙息导览｜新手向玩法介绍及首日规划", "2025-01-17", "https://www.taptap.cn/moment/629237455572176540"),
    ("CN-OFFICIAL-040", "结果公示｜二阶段蓝紫海王挑战赛", "2025-05-18", "https://www.taptap.cn/moment/673279962911870369"),
    ("CN-OFFICIAL-041", "策划FAQ｜S2赛季答疑", "2025-05-28", "https://www.taptap.cn/moment/676947597348308623"),
    ("CN-OFFICIAL-042", "精选召唤II｜冰光元素限时召唤", "2025-06-09", "https://www.taptap.cn/moment/681261107985252830"),
    ("CN-OFFICIAL-043", "精选召唤III｜鼓舞流派召唤", "2026-06-02", "https://www.taptap.cn/moment/810926142029562826?group_id=335048"),
    ("CN-OFFICIAL-044", "定向召唤I｜火黯元素限时召唤", "2025-06-06", "https://www.taptap.cn/moment/680179465002681760"),
    ("CN-OFFICIAL-046", "圣谕辉光召唤｜弥菈希亚专属召唤", "2026-06-26", "https://www.taptap.cn/moment/819642937838141817"),
    ("CN-OFFICIAL-047", "圣谕辉光召唤｜弥菈希亚专属召唤", "2026-08-17", "https://www.taptap.cn/moment/838465330899586585"),
]
story.append(table(["ID", "标题/日期", "URL"], [[sid, f"{title}<br/>{date}", url] for sid, title, date, url in sources], [28, 64, 85], font=6.1))
story += [Spacer(1, 5 * mm), P("版本说明", "H2CN"),
          P("报告生成于2026-10-22，结论面向370区S1 Day1。后续卡池、活动资格和数值可能变化；凡涉及当前客户端的内容，以370游戏内页面为最终准绳。研究建议与来源事实已分开书写，未实测项不作确定承诺。", "CN"),
          Spacer(1, 10 * mm), HRFlowable(width="100%", thickness=1, color=LINE),
          Spacer(1, 4 * mm), P("END OF REPORT", "Tiny")]


doc = ReportDoc(OUT)
doc.build(story)
print(OUT)
