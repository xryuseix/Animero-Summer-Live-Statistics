use clap::Clap;
use make_setlist::fetch::make_2009;
use make_setlist::fetch::make_2016;
use make_setlist::fetch::make_2017;
use make_setlist::fetch::make_2018;
use make_setlist::fetch::make_2019;

#[derive(Clap, Debug)]
#[clap(
    name = "make_setlist",
    version = "0.1.0",
    author = "xryuseix",
    about = "Make Anisama setlist"
)]
struct Opts {
    #[clap(name = "NUMBER")]
    year: Option<i32>,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let opts = Opts::parse();
    match opts.year {
        Some(year) => match year {
            2009 => make_2009::make_setlist_2009()?,
            2016 => make_2016::make_setlist_2016()?,
            2017 => make_2017::make_setlist_2017()?,
            2018 => make_2018::make_setlist_2018()?,
            2019 => make_2019::make_setlist_2019()?,
            _ => return Ok(()),
        },
        None => {
            println!("USAGE: cargo run [OPTIONS] [--] [args(~2019)]");
            return Ok(());
        }
    };
    Ok(())
}
