use reqwest::blocking;
use scraper::{Html, Selector};
use regex::Regex;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // リクエスト
    let body = blocking::get("https://anisama.tv/2019/setlist")?.text()?;
    // HTMLをパース
    let document = Html::parse_document(&body);
    // セレクターをパース
    let selector_row = Selector::parse(".setlist_table > tbody > tr").unwrap();

    // セットリストを取得
    for row in document.select(&selector_row) {
        let mut content = row.text().collect::<Vec<_>>();
        let num = content[0];
        let song = content[1];
        
        // アーティスト名の先頭に入っている" / "を削除
        let mut artist = content[2].chars().skip(3).collect::<String>();
        
        // Jam Projectに入っているノーブレークスペースを削除
        let re = Regex::new(r"\u{a0}").unwrap();
        artist = re.replace_all(&artist, "").to_string();
        println!("{:?}", artist);
    }

    Ok(())
}
