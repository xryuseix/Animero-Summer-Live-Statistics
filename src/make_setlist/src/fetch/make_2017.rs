use regex::Regex;
use reqwest::blocking;
use scraper::{Html, Selector};

use crate::dump_csv::dump_csv;

pub fn make_setlist_2017() -> Result<(), Box<dyn std::error::Error>> {
    // リクエスト
    let body = blocking::get("https://anisama.tv/2017/special/setlist.html")?.text()?;
    // HTMLをパース
    let document = Html::parse_document(&body);
    // セレクターをパース
    let selector_row = Selector::parse(".setlist_table > tbody > tr").unwrap();

    let mut setlist = Vec::new();

    // セットリストを取得
    for row in document.select(&selector_row) {
        let mut content = row.text().map(|s| s.to_string()).collect::<Vec<String>>();

        // アーティスト名の先頭に入っている" / "を削除
        // おジャ魔女でBANBANの時だけテーブル形式が違う
        if content[1] != "おジャ魔女でBAN" {
            let idx = content[2].char_indices().nth(3).unwrap().0;
            content[2] = content[2][idx..].to_string();
        } else {
            let idx = content[3].char_indices().nth(3).unwrap().0;
            content[2] = content[3][idx..].to_string();
            content.pop();
        }
        // ノーブレークスペースを削除
        let re = Regex::new(r"\u{a0}$").unwrap();
        content[2] = re.replace_all(&content[2], "").to_string();

        // setlistへ代入
        setlist.push(content);
    }

    dump_csv(&setlist, "2017".to_string())?;

    Ok(())
}
