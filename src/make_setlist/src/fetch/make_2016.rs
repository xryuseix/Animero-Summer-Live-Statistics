use regex::Regex;
use reqwest::blocking;
use scraper::{Html, Selector};

use crate::dump_csv::dump_csv;

pub fn make_setlist_2016() -> Result<(), Box<dyn std::error::Error>> {
    // リクエスト
    let body = blocking::get("https://anisama.tv/2016/special/setlist.html")?.text()?;
    // HTMLをパース
    let document = Html::parse_document(&body);
    // セレクターをパース
    let selector_row = Selector::parse(".setlist_table > tbody > tr").unwrap();

    let mut setlist = Vec::new();

    // セットリストを取得
    for row in document.select(&selector_row) {
        let content = row.text().map(|s| s.to_string()).collect::<Vec<String>>();
        let mut row = Vec::new();

        // 曲番号
        row.push(content[0].to_string());

        // 曲名と歌手名
        let re = Regex::new(r" / ").unwrap();
        for part in re.split(&content[1]) {
            row.push(part.to_string());
        }
        if row[1] == "PLANET".to_string() {
            row[1] = row[1].clone() + " / ";
            row[1] = row[1].clone() + row[2].as_str();
            row[2] = row[3].clone();
            row.pop();
        }

        // setlistへ代入
        setlist.push(row);
    }

    dump_csv(&setlist, "2016".to_string())?;

    Ok(())
}
