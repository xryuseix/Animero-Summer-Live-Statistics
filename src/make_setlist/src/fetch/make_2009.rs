use reqwest::blocking;
use scraper::{Html, Selector};
use encoding_rs;

pub fn make_setlist_2009() -> Result<(), Box<dyn std::error::Error>> {
    // リクエスト
    let body = blocking::get("https://anisama.tv/2009/whatsnew/index.html")?.text()?;
    // HTMLをパース
    let document = Html::parse_document(&body);
    // セレクターをパース
    let selector_row = Selector::parse("#main_cnt > div:nth-child(n+7):nth-child(-n+8) > div > table > tbody > tr > .text").unwrap();


    // セットリストを取得
    for row in document.select(&selector_row) {
        let content = row.text().map(|s| s.to_string()).collect::<Vec<String>>();
        let title = &*content[0];
        let (res, _, _) = encoding_rs::SHIFT_JIS.decode(title.as_bytes());
        // TODO: 文字化けが取れない
        let text = res.into_owned();
        println!("{}", text);
        println!("{:?}", content);
    }

    Ok(())
}