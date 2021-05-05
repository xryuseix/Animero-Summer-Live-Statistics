mod make_2019;
pub use crate::make_2019::make_setlist_2019;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    make_setlist_2019()?;
    Ok(())
}
