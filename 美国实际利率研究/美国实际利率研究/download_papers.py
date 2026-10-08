#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量下载美国实际利率研究相关论文PDF
"""

import os
import re
import time
import requests
from urllib.parse import urljoin, urlparse

# 下载目录
DOWNLOAD_DIR = r"D:\Obsidian 仓库\obsidian仓库\美国实际利率研究\美国实际利率研究\论文PDF"

# 论文列表：(文件名, 下载URL, 类型)
# 类型: direct=直接PDF链接, page=需要从页面找PDF
PAPERS = [
    # 一、r* 储蓄-投资框架
    ("01_Bernanke_2005_Global_Saving_Glut.pdf", "https://www.federalreserve.gov/boarddocs/speeches/2005/20050414/default.htm", "page"),
    ("02_Rachel_Smith_2015_Secular_Drivers.pdf", "https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2015/secular-drivers-of-the-global-real-interest-rate.pdf", "direct"),
    ("03_IMF_2014_WEO_Chapter3.pdf", "https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2014/01/pdf/_c3pdf.pdf", "direct"),
    ("04_HLW_2017_Measuring_Natural_Rate.pdf", "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr715.pdf", "direct"),  # NY Fed staff report版本
    ("05_Lubik_Matthes_2015_Calculating_Natural_Rate.pdf", "https://fraser.stlouisfed.org/files/docs/historical/frbrich/econbrief/frbrich_eb_15-10.pdf", "direct"),
    
    # 二、生产率与投资
    ("06_Gordon_2012_Is_US_Economic_Growth_Over.pdf", "https://www.nber.org/system/files/working_papers/w18315/w18315.pdf", "direct"),  # 替代Gordon 2016书籍
    ("07_Fernald_2014_TFP.pdf", "https://fraser.stlouisfed.org/files/docs/historical/frbsf/workingpapers/frbsf_wp2012-19.pdf", "direct"),
    ("08_GHK_1997_Investment_Specific_Tech_Change.pdf", "https://www.jstor.org/stable/2951349", "page"),  # JSTOR需要处理
    
    # 三、期限结构理论
    ("09_Vayanos_Vila_2021_Preferred_Habitat.pdf", "https://www.nber.org/system/files/working_papers/w15487/w15487.pdf", "direct"),
    ("10_Greenwood_Vayanos_2014_Bond_Supply.pdf", "https://academic.oup.com/rfs/article-pdf/27/3/663/1581525/hht127.pdf", "direct"),
    ("11_GHV_2024_Supply_Demand_Term_Structure.pdf", "https://www.nber.org/system/files/working_papers/w31879/w31879.pdf", "direct"),
    
    # 四、QE/QT与期限溢价
    ("12_DAmico_2012_Fed_LSAP.pdf", "https://www.federalreserve.gov/pubs/feds/2012/201285/201285pap.pdf", "direct"),
    ("13_Li_Wei_2013_Term_Structure_Supply_Factors.pdf", "https://www.federalreserve.gov/pubs/feds/2012/201237/201237pap.pdf", "direct"),
    ("14_DKW_Tips_from_TIPS.pdf", "https://www.federalreserve.gov/pubs/feds/2014/201424/201424pap.pdf", "direct"),
    ("15_ACM_2013_Pricing_Term_Structure.pdf", "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr340.pdf", "direct"),
    ("16_Kim_Wright_2005_Three_Factor_Model.pdf", "https://www.federalreserve.gov/pubs/feds/2005/200533/200533pap.pdf", "direct"),
    ("17_Christensen_Rudebusch_2012_QE_Response.pdf", "https://www.frbsf.org/wp-content/uploads/wp12-06bk1.pdf", "direct"),
    
    # 五、财政债务
    ("18_Elmendorf_Mankiw_1999_Government_Debt.pdf", "https://www.nber.org/system/files/working_papers/w6470/w6470.pdf", "direct"),
    ("19_Engen_Hubbard_2005_Federal_Debt_Interest_Rates.pdf", "https://www.nber.org/system/files/working_papers/w10681/w10681.pdf", "direct"),
    ("20_Laubach_2009_Interest_Rate_Effects.pdf", "https://www.federalreserve.gov/pubs/feds/2003/200312/200312pap.pdf", "direct"),
    
    # 六、主权风险
    ("21_Hilscher_Nosbusch_2010_Sovereign_Risk.pdf", "https://academic.oup.com/rof/article-pdf/14/2/235/314139/rfq005.pdf", "direct"),
    ("22_Borri_Verdelhan_2012_Sovereign_Risk_Premia.pdf", "https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID1343746_code.pdf", "direct"),
    ("23_Farhi_Maggiori_2018_International_Monetary_System.pdf", "https://www.nber.org/system/files/working_papers/w22295/w22295.pdf", "direct"),
    
    # 七、金融中介
    ("24_He_Krishnamurthy_2013_Intermediary_Asset_Pricing.pdf", "https://mfm.uchicago.edu/wp-content/uploads/2020/07/He-Krishnamurthy-Intermediary-Asset-Pricing.pdf", "direct"),
    ("25_Brunnermeier_Sannikov_2014_Macro_Financial_Sector.pdf", "https://www.princeton.edu/~markus/research/papers/macro_finance.pdf", "direct"),
    ("26_Adrian_Shin_2010_Liquidity_Leverage.pdf", "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr328.pdf", "direct"),
    
    # 八、MMF
    ("27_Aldasoro_Doerr_2023_Who_Borrows_MMF.pdf", "https://www.bis.org/publ/qtrpdf/r_qt2312d.pdf", "direct"),
    ("28_Doerr_Eren_Malamud_2023_MMF_Near_Money.pdf", "https://www.bis.org/publ/work1096.pdf", "direct"),
    
    # 九、安全资产
    ("29_Krishnamurthy_VissingJorgensen_2012_Treasury_Debt.pdf", "https://www.nber.org/system/files/working_papers/w12881/w12881.pdf", "direct"),
    
    # 十、黄金
    ("30_Barsky_Summers_1988_Gibson_Paradox.pdf", "https://www.nber.org/system/files/working_papers/w1680/w1680.pdf", "direct"),
    ("31_Baur_Lucey_2010_Gold_Hedge_Safe_Haven.pdf", "https://brianmlucey.com/wp-content/uploads/2011/05/gold_safehavenorhedge_fr.pdf", "direct"),
    ("32_Gorton_Ordonez_2013_Safe_Assets.pdf", "https://www.nber.org/system/files/working_papers/w18732/w18732.pdf", "direct"),
]

# 请求头，模拟浏览器
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/pdf,application/octet-stream,*/*',
    'Accept-Language': 'en-US,en;q=0.9',
}


def download_pdf(filename, url, url_type="direct"):
    """下载单个PDF文件"""
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    
    # 如果文件已存在且大小正常，跳过
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1024:
        print(f"[跳过] {filename} (已存在)")
        return True
    
    try:
        print(f"[下载] {filename}")
        print(f"       来源: {url}")
        
        response = requests.get(url, headers=HEADERS, timeout=60, allow_redirects=True, stream=True)
        response.raise_for_status()
        
        # 检查是否真的是PDF
        content_type = response.headers.get('content-type', '').lower()
        if 'pdf' not in content_type and url_type == 'direct':
            # 有些服务器不返回正确的content-type，但文件确实是PDF
            pass
        
        # 写入文件
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        file_size = os.path.getsize(filepath)
        
        # 验证文件是否是PDF（检查magic bytes）
        with open(filepath, 'rb') as f:
            header = f.read(4)
            if header != b'%PDF':
                print(f"       ⚠️  警告: 可能不是PDF文件 (size: {file_size} bytes)")
                # 尝试从HTML页面找PDF链接
                if url_type == 'page':
                    print(f"       尝试从页面提取PDF链接...")
                    # 重新获取页面内容
                    page_response = requests.get(url, headers=HEADERS, timeout=30)
                    pdf_match = re.search(r'href=["\']([^"\']+\.pdf)["\']', page_response.text, re.IGNORECASE)
                    if pdf_match:
                        pdf_url = urljoin(url, pdf_match.group(1))
                        print(f"       找到PDF链接: {pdf_url}")
                        return download_pdf(filename, pdf_url, "direct")
                    else:
                        print(f"       ❌ 无法找到PDF链接")
                        os.remove(filepath) if os.path.exists(filepath) else None
                        return False
        
        print(f"       ✅ 成功 ({file_size:,} bytes)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"       ❌ 下载失败: {e}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return False
    except Exception as e:
        print(f"       ❌ 错误: {e}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("美国实际利率研究论文批量下载")
    print("=" * 60)
    print(f"下载目录: {DOWNLOAD_DIR}")
    print(f"论文数量: {len(PAPERS)}")
    print("=" * 60)
    print()
    
    # 确保目录存在
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    # 统计
    success_count = 0
    fail_count = 0
    failed_papers = []
    
    # 逐一下载
    for i, (filename, url, url_type) in enumerate(PAPERS, 1):
        print(f"[{i}/{len(PAPERS)}] ", end="")
        if download_pdf(filename, url, url_type):
            success_count += 1
        else:
            fail_count += 1
            failed_papers.append((filename, url))
        print()
        
        # 礼貌延迟，避免请求过快
        time.sleep(1)
    
    # 汇总
    print("=" * 60)
    print("下载完成汇总")
    print("=" * 60)
    print(f"成功: {success_count} 篇")
    print(f"失败: {fail_count} 篇")
    
    if failed_papers:
        print("\n失败的论文:")
        for filename, url in failed_papers:
            print(f"  - {filename}")
            print(f"    {url}")
    
    print()
    print(f"文件保存位置: {DOWNLOAD_DIR}")


if __name__ == "__main__":
    main()
