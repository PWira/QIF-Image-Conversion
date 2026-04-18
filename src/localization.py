"""
Localization/i18n module for Image Resolver.
Supports English (default) and Indonesian.
"""

# Translation dictionary
TRANSLATIONS = {
    "en": {
        # Window and tabs
        "title": "Image Converter & Resizer",
        "tab_convert": "Convert",
        "tab_resize": "Resize",
        "tab_batch": "Batch",
        
        # Common UI
        "log": "Log",
        "format_output": "Output format",
        "quality": "Quality",
        "width_px": "Width (px)",
        "height_px": "Height (px)",
        "mode": "Mode",
        "select_btn": "Browse...",
        
        # Tab: Convert
        "tab_convert_label": "Convert",
        "file_input": "Input file",
        "file_output": "Output file",
        "resize_optional": "Resize (optional)",
        "mode_resize": "Resize mode",
        "resize_fit": "Proportional (fit)",
        "resize_exact": "Exact",
        "resize_thumbnail": "Thumbnail (crop)",
        "resize_percent": "Percentage (%)",
        "btn_convert_now": "Convert Now",
        "tooltip_quality": "Quality only applies to JPEG, WEBP, AVIF",
        "tooltip_width": "Leave empty if not used",
        "tooltip_height": "Leave empty if not used",
        
        # Tab: Resize
        "tab_resize_label": "Resize",
        "scale_percent": "Scale (%)",
        "max_width": "Max width",
        "max_height": "Max height",
        "btn_resize_now": "Resize Now",
        "tooltip_scale": "Example: 50 = half size",
        "tooltip_max_w": "Maximum width limit",
        "tooltip_max_h": "Maximum height limit",
        
        # Tab: Batch
        "tab_batch_label": "Batch",
        "folder_input": "Input folder",
        "folder_output": "Output folder",
        "recursive": "Process subfolders (recursive)",
        "btn_batch_start": "Start Batch",
        
        # Messages
        "error_input_missing": "Missing input",
        "error_select_file": "Please select input and output files first.",
        "error_select_folder": "Please select input and output folders.",
        "info_files_found": "files found in",
        "info_completed": "Completed:",
        "info_ok": "successful",
        "info_err": "failed",
        
        # Log messages (symbols kept, text translated)
        "log_success": "✓",
        "log_error": "✗",
        "log_arrow": "→",
    },
    "id": {
        # Window and tabs
        "title": "Image Converter & Resizer",
        "tab_convert": "Konversi",
        "tab_resize": "Resize",
        "tab_batch": "Batch",
        
        # Common UI
        "log": "Log",
        "format_output": "Format output",
        "quality": "Kualitas",
        "width_px": "Lebar (px)",
        "height_px": "Tinggi (px)",
        "mode": "Mode",
        "select_btn": "Pilih...",
        
        # Tab: Convert
        "tab_convert_label": "Konversi",
        "file_input": "File input",
        "file_output": "File output",
        "resize_optional": "Resize (opsional)",
        "mode_resize": "Mode resize",
        "resize_fit": "Proporsional (fit)",
        "resize_exact": "Tepat (exact)",
        "resize_thumbnail": "Thumbnail (crop)",
        "resize_percent": "Persentase (%)",
        "btn_convert_now": "Konversi Sekarang",
        "tooltip_quality": "Hanya berlaku untuk JPEG, WEBP, AVIF",
        "tooltip_width": "Kosongkan jika tidak dipakai",
        "tooltip_height": "Kosongkan jika tidak dipakai",
        
        # Tab: Resize
        "tab_resize_label": "Resize",
        "scale_percent": "Skala (%)",
        "max_width": "Maks lebar",
        "max_height": "Maks tinggi",
        "btn_resize_now": "Resize Sekarang",
        "tooltip_scale": "Contoh: 50 = setengah ukuran",
        "tooltip_max_w": "Batas lebar maksimal",
        "tooltip_max_h": "Batas tinggi maksimal",
        
        # Tab: Batch
        "tab_batch_label": "Batch",
        "folder_input": "Folder input",
        "folder_output": "Folder output",
        "recursive": "Masuk subfolder (recursive)",
        "btn_batch_start": "Mulai Batch Konversi",
        
        # Messages
        "error_input_missing": "Input kurang",
        "error_select_file": "Pilih file input dan output terlebih dahulu.",
        "error_select_folder": "Pilih folder input dan output.",
        "info_files_found": "file ditemukan di",
        "info_completed": "Selesai:",
        "info_ok": "berhasil",
        "info_err": "gagal",
        
        # Log messages (symbols kept, text translated)
        "log_success": "✓",
        "log_error": "✗",
        "log_arrow": "→",
    },
}


class I18n:
    """Localization manager for Image Resolver."""
    
    def __init__(self, language: str = "en"):
        """
        Initialize with language.
        
        Args:
            language: Language code ("en" or "id")
        """
        self.language = language if language in TRANSLATIONS else "en"
        self.translations = TRANSLATIONS[self.language]
    
    def set_language(self, language: str):
        """Set language and reload translations."""
        if language in TRANSLATIONS:
            self.language = language
            self.translations = TRANSLATIONS[self.language]
    
    def get(self, key: str, default: str = "") -> str:
        """
        Get translated string.
        
        Args:
            key: Translation key
            default: Default value if key not found
        
        Returns:
            Translated string
        """
        return self.translations.get(key, default)
    
    def __call__(self, key: str) -> str:
        """Allow calling instance as function: i18n(key)."""
        return self.get(key)


# Global instance
_i18n = I18n("en")


def get_i18n() -> I18n:
    """Get global i18n instance."""
    return _i18n


def set_language(language: str):
    """Set global language."""
    _i18n.set_language(language)
