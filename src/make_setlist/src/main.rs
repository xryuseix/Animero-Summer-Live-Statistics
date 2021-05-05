use clap::Clap;
mod dump_csv;
mod make_2018;
mod make_2019;
pub use crate::dump_csv::dump_csv;
pub use crate::make_2018::make_setlist_2018;
pub use crate::make_2019::make_setlist_2019;

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
            2018 => make_setlist_2018()?,
            2019 => make_setlist_2019()?,
            _ => return Ok(()),
        },
        None => return Ok(()),
    };
    Ok(())
}
