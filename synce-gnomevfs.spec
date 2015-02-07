# NOTE: deprecated in favour of synce-gvfs
Summary:	GnomeVFS module for accessing Windows CE and Pocket PC devices
Summary(pl.UTF-8):	Moduł GnomeVFS służący do dostępu do urządzeń Windows CE i Pocket PC
Name:		synce-gnomevfs
Version:	0.13
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	6069ead295f8d26362a1fab6083b40a8
Patch0:		%{name}-no_cxx.patch
URL:		http://www.synce.org/
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	synce-librapi2-devel >= 0.12
BuildRequires:	synce-libsynce-devel >= 0.12
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	hicolor-icon-theme
%requires_ge_to	synce-librapi2 synce-librapi2-devel
%requires_ge_to	synce-libsynce synce-libsynce-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GnomeVFS is a GnomeVFS module for accessing Windows CE and
Pocket PC devices. It is part of the SynCE project:
<http://www.synce.org/>.

%description -l pl.UTF-8
SynCE-GnomeVFS to moduł GnomeVFS służący do dostępu do urządzeń
Windows CE i Pocket PC. Jest on częścią projektu SynCE:
<http://www.synce.org/>.

%prep
%setup -q
%patch0 -p0

%build
cp -f /usr/share/automake/config.* .
%configure \
	--disable-update-mime-database
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/synce-trayicon/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database

%postun
%update_icon_cache hicolor
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/synce-in-computer-folder
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/libsyncevfs.so
%attr(755,root,root) %{_libdir}/synce-trayicon/modules/gnomevfs-trayicon-module.so
%{_sysconfdir}/gnome-vfs-2.0/modules/synce-module.conf
%{_datadir}/mime/packages/synce-gnomevfs.xml
%{_iconsdir}/hicolor/48x48/apps/synce-gnomevfs.png
# dir shared with synce-rra, synce-software-manager, synce-trayicon
%dir %{_datadir}/synce
%attr(755,root,root) %{_datadir}/synce/synce-in-computer-folder.sh
%{_mandir}/man1/synce-in-computer-folder.1*
